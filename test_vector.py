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

    def test_magnitude(self):
        vector = Vector([-0.221, 7.437])
        np.testing.assert_almost_equal(vector.length(), 7.44028292473, 3)

        vector = Vector([8.813, -1.331, -6.247])
        np.testing.assert_almost_equal(vector.length(), 10.8841875673, 3)

    def test_normalize(self):
        vector = Vector([5.581, -2.136])
        expected_result = [0.9339352140866403, -0.35744232526233]
        np.testing.assert_almost_equal(list(vector.normalize()), expected_result, 3)

        vector = Vector([1.996, 3.108, -4.554])
        expected_result = [0.3404012959433014, 0.5300437012984873, -0.7766470449528029]
        np.testing.assert_almost_equal(list(vector.normalize()), expected_result, 3)

if __name__ == '__main__':
    unittest.main()
