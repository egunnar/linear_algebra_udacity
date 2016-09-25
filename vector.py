import math

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


