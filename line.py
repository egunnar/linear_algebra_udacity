from decimal import Decimal, getcontext
import numpy as np

from vector import Vector

getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def intersection(self, line):
        # if no intersection or infinite intersection return None
        if self.is_parallel(line):
            return None
        if self.is_equal(line):
            return None

        # The formula
        # Ax1 + By1 = k1 ( <- this is self)
        # Cx2 + Dy2 = k2 ( <- this is line)
        # x = (Dk1 - Bk2) / (AD - BC)
        # y = (-Ck1 + Ak2) / (AD - BC)

        A = self.normal_vector[0]
        B = self.normal_vector[1]
        C = line.normal_vector[0]
        D = line.normal_vector[1]
        x = ((D * self.constant_term) - (B * line.constant_term)) / \
            ((A * D) - (B * C))
        y = ((-C * self.constant_term) + (A * line.constant_term)) / \
            ((A * D) - (B * C))
        return Vector([x, y])


    def is_parallel(self, line):
        return self.normal_vector.is_parallel(line.normal_vector)


    def is_equal(self, line):

        # Might be a weird way to see if the lines are equal but it
        # scales well to higher dimensions

        base_point1 = self.basepoint
        base_point2 = line.basepoint

        connecting_vector = base_point1 - base_point2

        def get_othogonal_vector(vector):
            tmp = vector[0]
            vector[0] = vector[1]
            vector[1] = -tmp
            return vector

        test1 = get_othogonal_vector(connecting_vector)
        if not(test1.is_parallel(self.normal_vector)):
            return False
        if not(test1.is_parallel(line.normal_vector)):
            return False
        return True


    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = [0]*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = 0
        self.constant_term = constant_term

        self.set_basepoint()


    def set_basepoint(self):
        # note, the base point is simply a arbitray point on the line
        try:
            n = self.normal_vector
            c = self.constant_term
            basepoint_coords = [0]*self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = 0
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not np.isclose(item, 0):
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
