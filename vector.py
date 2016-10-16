import math
import numpy as np

class Vector():

    def __init__(self, values):
        self.values = values
        self.dimension = len(values)

    def __len__(self):
        return self.dimension

    def __add__(self, values_to_add):
        if len(values_to_add) != self.dimension:
            raise ValueError('Dimension of vector is {} and vector ' \
                'to add is {}'.format(self.dimension, len(values_to_add)))
        new_values = []
        for i, j in zip(self.values, values_to_add):
            new_values.append(i + j)

        return Vector(new_values)

    def __sub__(self, values_to_subtract):
        if len(values_to_subtract) != self.dimension:
            raise ValueError('Dimension of vector is {} and vector ' \
                'to subtract is {}'.format(self.dimension, len(values_to_subtract)))
        new_values = []
        for i, j in zip(self.values, values_to_subtract):
            new_values.append(i - j)

        return Vector(new_values)

    def scalar_multipile(self, scalar):
        return Vector([i * scalar for i in self.values])

    def __iter__(self):
        return iter(self.values)

    def __str__(self):
        return "Vector ({})".format(self.values)

    def normalize(self):
        ''' Return a normalized version of the vector. This is the unit
            vector of length 1 in the same direction.'''
        scale_by = 1.0 / self.length()
        return self.scalar_multipile(scale_by)

    def length(self):
        ''' Return the length of the vector. Not the dimension.'''
        sum_squared = 0
        for i in self.values:
            sum_squared += i * i
        return math.sqrt(sum_squared)

    def calculate_inner_product(self, vector_to_multiple):
        ''' Note inner product is the same as dot product '''

        if len(vector_to_multiple) != self.dimension:
            raise ValueError('Dimension of vector is {} and vector ' \
                'to multiple is {}'.format(self.dimension, \
                vector_to_multiple.dimension))

        result = 0.0
        for index, vector_item  in enumerate(vector_to_multiple):
            result += (self.values[index] * vector_item)
        return result

    def angle_between_vectors(self, input_vector):
        for_cos = self.normalize().calculate_inner_product(input_vector.normalize())

        # due to floating point errors if value is slighly larger than 1 or
        # less than -1 acos will explode as in math it is impossible to for
        # cosine to be outside of [-1, 1]
        if np.isclose(for_cos, -1):
            for_cos = -1
        if np.isclose(for_cos, 1):
            for_cos = 1

        return math.acos(for_cos)

    def angle_between_vectors_in_degrees(self, input_vector):
        return math.degrees(self.angle_between_vectors(input_vector))

    def is_zero_vector(self):
        for i in self.values:
            if i != 0:
                return False
        return True


    def is_parallel(self, input_vector):

        if self.is_zero_vector() or input_vector.is_zero_vector():
            return True
        angle = self.angle_between_vectors_in_degrees(input_vector)
        if np.isclose(angle, 0) or np.isclose(angle, 180):
            return True

        return False

    def is_orthogonal(self, input_vector):

        dot_product = self.calculate_inner_product(input_vector)
        if np.isclose(dot_product, 0):
            return True
        else:
            return False

    def projected_onto(self, v_project_onto):
        v_unit_vector = v_project_onto.normalize()
        tmp_scalar = self.calculate_inner_product(v_unit_vector)
        return v_unit_vector.scalar_multipile(tmp_scalar)

    def orthogonal_vector(self, w_project_onto):
        return self - self.projected_onto(w_project_onto)

    def cross_product(self, v):

        if (len(self) != 3  or len(v) != 3):
            raise Exception('cross product is 3 dimensions only. if you'\
                ' are using 2 dimensions put a 0 for both z values')
        X = 0
        Y = 1
        Z = 2
        return Vector([
            self.values[Y] * v.values[Z] - self.values[Z] * v.values[Y],
            self.values[Z] * v.values[X] - self.values[X] * v.values[Z],
            self.values[X] * v.values[Y] - self.values[Y] * v.values[X],
        ])

    def area_of_parrallelogram(self, v):
        return self.cross_product(v).length()

    def area_of_triangle(self, v):
        return .5 * self.cross_product(v).length()
