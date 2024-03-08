import unittest

from shape import Square, Rectangle

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.testData = (
            ( 4, 16, 16),
            (0, 0, 0),
        )
    
    def test_area(self):
        for length, area, _ in self.testData:
            mysquare = Square(length)
            self.assertEqual(mysquare.area(), area)

    
    def test_perimeter(self):
        for length, _, perimeter in self.testData:
            mysquare = Square(length)
            self.assertEqual(mysquare.perimeter(), perimeter)
    
    def test_negative_length_not_allowed(self):
        with self.assertRaises(ValueError):
            mysquare = Square(-4)

    def test_non_number_length_not_allowed(self):
        with self.assertRaises(TypeError):
            mysquare = Square("4")

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.testData = (
            ( 2, 5, 10, 14),
            (0, 1, 0, 2),
        )
    
    def test_area(self):
        for side1, side2, area, _ in self.testData:
            myrect = Rectangle(side1, side2)
            self.assertEqual(myrect.area(), area)

    
    def test_perimeter(self):
        for side1, side2, _, perimeter in self.testData:
            myrect = Rectangle(side1, side2)
            self.assertEqual(myrect.perimeter(), perimeter)
    
    def test_negative_length_not_allowed(self):
        with self.assertRaises(ValueError):
            myrect = Rectangle(0,-1)

    def test_non_number_length_not_allowed(self):
        with self.assertRaises(TypeError):
            myrect = Rectangle(4,"4")


if __name__ == "__main__":
    unittest.main() 
