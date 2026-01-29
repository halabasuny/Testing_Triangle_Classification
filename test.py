import unittest
from main import classify_triangle

class TestClassifyTriangle(unittest.TestCase):

    # ----- Invalid / Not a triangle -----
    def test_invalid_non_numeric(self):
        self.assertEqual(classify_triangle("3", 4, 5), "NotATriangle")
        self.assertEqual(classify_triangle(None, 4, 5), "NotATriangle")
        self.assertEqual(classify_triangle(True, 4, 5), "NotATriangle")  # bool should be rejected

    def test_invalid_non_positive(self):
        self.assertEqual(classify_triangle(0, 4, 5), "NotATriangle")
        self.assertEqual(classify_triangle(-3, 4, 5), "NotATriangle")

    def test_triangle_inequality(self):
        self.assertEqual(classify_triangle(1, 2, 3), "NotATriangle")   # equality boundary
        self.assertEqual(classify_triangle(1, 2, 4), "NotATriangle")   # violation
        self.assertEqual(classify_triangle(2, 3, 10), "NotATriangle")  # violation

    # ----- Basic classifications -----
    def test_equilateral(self):
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")
        self.assertEqual(classify_triangle(10, 10, 10), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles")
        self.assertEqual(classify_triangle(3, 2, 2), "Isosceles")
        self.assertEqual(classify_triangle(2, 3, 2), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    # ----- Right triangles (including isosceles right) -----
    def test_right_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")
        self.assertEqual(classify_triangle(5, 3, 4), "Scalene Right")  # order independent
        self.assertEqual(classify_triangle(8, 15, 17), "Scalene Right")

    def test_right_isosceles(self):
        self.assertEqual(classify_triangle(1, 1, 2 ** 0.5), "Isosceles Right")
        self.assertEqual(classify_triangle(5, 5, (50) ** 0.5), "Isosceles Right")

    def test_not_right(self):
        self.assertEqual(classify_triangle(2, 3, 4), "Scalene")
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles")

    # ----- Float handling -----
    def test_float_sides(self):
        self.assertEqual(classify_triangle(0.3, 0.4, 0.5), "Scalene Right")
        self.assertEqual(classify_triangle(1.5, 1.5, 1.5), "Equilateral")

if __name__ == "__main__":
    unittest.main()
