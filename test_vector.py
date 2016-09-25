from vector import Vector
import unittest
import numpy as np

class TestVector(unittest.TestCase):

    def test_addition(self):
        vector_1 = Vector([8.218, -9.341])
        vector_2 = Vector([-1.129, 2.111])
        expected_result = [7.089, -7.2299]
        np.testing.assert_almost_equal(list(vector_1 + vector_2),
            expected_result, 3)

    def test_substraction(self):
        vector_1 = Vector([7.119, 8.215])
        vector_2 = Vector([-8.223, 0.878])
        expected_result = [15.342, 7.337]
        np.testing.assert_almost_equal(list(vector_1 - vector_2),
            expected_result, 3)

    def test_scalar_multiplication(self):
        vector_1 = Vector([1.671, -1.012, -0.318])
        expected_result = [12.38211, -7.49892, -2.35638]
        np.testing.assert_almost_equal(list(vector_1.scalar_multipile(7.41)),
            expected_result, 3)

if __name__ == '__main__':
    unittest.main()
