from vector import Vector
from line import Line
import unittest
import numpy as np
from plane import Plane
from linsys import LinearSystem

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

    def test_inner_product(self):
        vector1 = Vector([7.887, 4.138])
        vector2 = Vector([-8.802, 6.776])
        result = vector1.calculate_inner_product(vector2)
        expected_result = -41.382286
        np.testing.assert_almost_equal(result, expected_result, 3)

        vector1 = Vector([-5.955, -4.904, -1.874])
        vector2 = Vector([-4.496, -8.755, 7.103])
        expected_result = 56.397178
        result = vector1.calculate_inner_product(vector2)
        np.testing.assert_almost_equal(result, expected_result, 3)


    def test_angle_between(self):
        vector1 = Vector([3.183, -7.627])
        vector2 = Vector([-2.668, 5.319])
        expected_result = 3.07202630984
        result = vector1.angle_between_vectors(vector2)
        np.testing.assert_almost_equal(result, expected_result, 3)

        vector1 = Vector([7.35, .221, 5.188])
        vector2 = Vector([2.751, 8.259, 3.985])
        expected_result = 60.2758112052
        result = vector1.angle_between_vectors_in_degrees(vector2)
        np.testing.assert_almost_equal(result, expected_result, 3)

    def test_parallel_and_orthogonal(self):
        vectors_to_check = (
            {
                'vectors':  ([-7.579, -7.88], [22.737, 23.64]),
                'parallel': True,
                'orthogonal': False
            },
            {
                'vectors': ([-2.029, 9.97, 4.172], [-9.231, -6.639, -7.245]),
                'parallel': False,
                'orthogonal': False
            },
            {
                'vectors': ([-2.328, -7.284, -1.214], [-1.821, 1.072, -2.94]),
                'parallel': False,
                'orthogonal': True
            },
            {
                'vectors': ([2.118, 4.827], [0, 0]),
                'parallel': True,
                'orthogonal': True
            },
        )

        for test_info in vectors_to_check:
            v1 = Vector(test_info['vectors'][0])
            v2 = Vector(test_info['vectors'][1])
            v1.is_parallel(v2)
            parallel = self.assertEqual(v1.is_parallel(v2), test_info['parallel'])
            orthogonal = self.assertEqual(v1.is_orthogonal(v2), test_info['orthogonal'])

    def test_projection(self):

        v = Vector([3.039, 1.879])
        b = Vector([0.825, 2.036])
        result = v.projected_onto(b)
        expected_result = [1.08260, 2.6717]
        np.testing.assert_almost_equal(list(result),
            expected_result, 3)

        # test orthogonal to projection
        v = Vector([-9.88, -3.264, -8.159])
        w = Vector([-2.155, -9.353, -9.473])
        result = v.orthogonal_vector(w)
        expected_result = [-8.35008, 3.37606, -1.433746]
        np.testing.assert_almost_equal(list(result),
            expected_result, 3)

        # test can break into 2 vector components
        v = Vector([3.009,-6.172,3.692,-2.51])
        w = Vector([6.404,-9.144,2.759,8.718])
        b = v.projected_onto(w)
        expected_result = [1.9685, -2.8107607, 0.84808, 2.6798]
        np.testing.assert_almost_equal(list(b), expected_result, 3)

        o = v.orthogonal_vector(w)
        expected_result  = [1.0404838, -3.361239, 2.843915, -5.1898]
        np.testing.assert_almost_equal(list(o), expected_result, 3)

    def test_cross_product(self):
        v = Vector([8.462, 7.893, -8.187])
        w = Vector([6.984, -5.975, 4.778])

        expected_result = [-11.20457, -97.6094, -105.68516]
        result = v.cross_product(w)
        np.testing.assert_almost_equal(list(result), expected_result, 3)

        v = Vector([-8.987, -9.838, 5.031])
        w = Vector([-4.268, -1.861, -8.866])
        expected_result = 142.12222
        result = v.area_of_parrallelogram(w)
        np.testing.assert_almost_equal(result, expected_result, 3)

        v = Vector([1.5, 9.547, 3.691])
        w = Vector([-6.007, 0.124, 5.772])
        result = v.area_of_triangle(w)
        expected_result = 42.56493739941894
        np.testing.assert_almost_equal(result, expected_result, 3)

    def test_line_functions(self):
        lines_to_test = (
            {
                'lines':
                    (
                        Line(Vector([4.046, 2.836]), 1.21),
                        Line(Vector([10.115, 7.09]), 3.025)
                    ),
                'equal': True,
                'parallel': True,
                'intersection': None,
            },
            {
                'lines':
                    (
                        Line(Vector([7.204, 3.182]), 8.68),
                        Line(Vector([8.172, 4.114]), 9.883)
                    ),
                'equal': False,
                'parallel': False,
                'intersection': (1.1727766354646414, 0.07269551166333184),
            },
            {
                'lines':
                    (
                        Line(Vector([1.182, 5.562]), 6.744),
                        Line(Vector([1.773, 8.343]), 9.525)
                    ),
                'equal': False,
                'parallel': True,
                'intersection': None,
            }
        )
        for line_test_info in lines_to_test:
            line1 = line_test_info['lines'][0]
            line2 = line_test_info['lines'][1]
            self.assertEqual(line1.is_parallel(line2),
                line_test_info['parallel'])
            self.assertEqual(line1.is_equal(line2), line_test_info['equal'])
            intersection_vector = line1.intersection(line2)
            if intersection_vector is None:
                self.assertIsNone(line_test_info['intersection'])
            else:
                np.testing.assert_almost_equal(
                    list(intersection_vector.values),
                    line_test_info['intersection'])

    def test_plane_functions(self):
        planes_to_test = (
            {
                'planes': (
                    Plane(Vector([-0.412, 3.806, 0.728]), -3.46),
                    Plane(Vector([1.03, -9.515, -1.82]), 8.65)
                ),
                'equal': True,
                'parallel': True,
            },
            {
                'planes': (
                    Plane(Vector([2.611, 5.528, 0.283]), 4.6),
                    Plane(Vector([7.715, 8.306, 5.342]), 3.76)
                ),
                'equal': False,
                'parallel': False,
            },
            {
                'planes': (
                    Plane(Vector([-7.926, 8.625, -7.212]), -7.952),
                    Plane(Vector([-2.642, 2.875, -2.404]), -2.443)
                ),
                'equal': False,
                'parallel': True,
            }
        )
        for plane_test_info in planes_to_test:
            plane1 = plane_test_info['planes'][0]
            plane2 = plane_test_info['planes'][1]
            self.assertEqual(plane1.is_parallel(plane2),
                plane_test_info['parallel'])
            self.assertEqual(plane1.is_equal(plane2), plane_test_info['equal'])

    def test_ge_functions(self):

        p0 = Plane(normal_vector=Vector([1,1,1]), constant_term=1)
        p1 = Plane(normal_vector=Vector([0,1,0]), constant_term=2)
        p2 = Plane(normal_vector=Vector([1,1,-1]), constant_term=3)
        p3 = Plane(normal_vector=Vector([1,0,-2]), constant_term=2)

        s = LinearSystem([p0, p1, p2, p3])
        s.swap_rows(0,1)
        self.assertTrue(s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3)

        s.swap_rows(1,3)
        self.assertTrue(s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0)

        s.swap_rows(3,1)
        self.assertTrue(s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3)

        s.multiply_coefficient_and_row(1,0)
        self.assertTrue(s[0] == p1)
        self.assertTrue(s[1] == p0)
        self.assertTrue(s[2] == p2)
        self.assertTrue(s[3] == p3)

        s.multiply_coefficient_and_row(-1,2)
        self.assertTrue(s[0] == p1 and s[1] == p0 and s[2] == \
            Plane(normal_vector=Vector([-1,-1,1]), constant_term=-3) \
            and s[3] == p3)

        s.multiply_coefficient_and_row(10,1)
        self.assertTrue(s[0] == p1 and \
            s[1] == Plane(normal_vector=Vector([10,10,10]),
                          constant_term=10) and
            s[2] == Plane(normal_vector=Vector([-1,-1,1]),
                          constant_term=-3) and
            s[3] == p3)

        s.add_multiple_times_row_to_row(0,0,1)
        self.assertTrue(s[0] == p1 and \
            s[1] == Plane(normal_vector=Vector([10,10,10]),
                          constant_term=10) and
            s[2] == Plane(normal_vector=Vector([-1,-1,1]),
                          constant_term=-3) and
            s[3] == p3)

        s.add_multiple_times_row_to_row(1,0,1)
        self.assertTrue(s[0] == p1 and \
            s[1] == Plane(normal_vector=Vector([10,11,10]),
                          constant_term=12) and
            s[2] == Plane(normal_vector=Vector([-1,-1,1]),
                          constant_term=-3) and
            s[3] == p3)

        # params coefficient, row_to_add, row_to_be_added_to
        s.add_multiple_times_row_to_row(-1,1,0)
        self.assertTrue(
            s[0] == Plane(normal_vector=Vector([-10,-10,-10]),
                          constant_term=-10) and
            s[1] == Plane(normal_vector=Vector([10,11,10]),
                          constant_term=12) and
            s[2] == Plane(normal_vector=Vector([-1,-1,1]),
                          constant_term=-3) and
            s[3] == p3)


if __name__ == '__main__':
    unittest.main()

