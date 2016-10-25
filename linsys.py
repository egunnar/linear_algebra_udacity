from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def swap_rows(self, row1, row2):
        tmp = self.planes[row1]
        self.planes[row1] = self.planes[row2]
        self.planes[row2] = tmp


    def multiply_coefficient_and_row(self, coefficient, row):
        vector = self.planes[row].get_normal_vector()
        for i, value in enumerate(vector):
            vector[i] = value * coefficient

        const = self.planes[row].get_constant_term()
        const = const * coefficient

        self.planes[row] = Plane(vector, constant_term= const)



    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):

        vector_to_add = self.planes[row_to_add].get_normal_vector()
        for i, value in enumerate(vector_to_add):
            vector_to_add[i] = value * coefficient
        const_to_add = self.planes[row_to_add].get_constant_term()
        const_to_add = const_to_add * coefficient

        vector_to_set = self.planes[row_to_be_added_to].get_normal_vector()
        for i, value in enumerate(vector_to_set):
            vector_to_set[i] = value + vector_to_add[i]
        const_to_set = self.planes[row_to_be_added_to].get_constant_term()
        const_to_set = const_to_set + const_to_add

        self.planes[row_to_be_added_to] = Plane(vector_to_set, constant_term= const_to_set)


    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps

