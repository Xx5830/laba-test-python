import math
import unittest

def area(a):
    '''
    принимает a (double) возвращает площадь квадрата со сторонами a
    параметры: a (double)
    возвращает: площадь квадрата (double)
    '''
    return a * a


def perimeter(a):
    '''
    принимает a (double) возвращает периметр квадрата со сторонами a
    параметры: a (double)
    возвращает: периметр квадрата (double)
    '''
    return 4 * a



class SquareTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        self.assertEqual(area(0), 0)
    
    def test_area_positive_integer(self):
        self.assertEqual(area(1), 1)
        self.assertEqual(area(2), 4)
        self.assertEqual(area(5), 25)
        self.assertEqual(area(10), 100)
    
    def test_area_positive_float(self):
        self.assertAlmostEqual(area(1.5), 2.25)
        self.assertAlmostEqual(area(2.5), 6.25)
        self.assertAlmostEqual(area(0.5), 0.25)
        self.assertAlmostEqual(area(3.14159), 3.14159 * 3.14159)
    
    def test_area_negative_side(self):
        self.assertEqual(area(-1), 1)
        self.assertEqual(area(-2), 4)
        self.assertEqual(area(-5), 25)
        self.assertAlmostEqual(area(-1.5), 2.25)
    
    def test_area_large_numbers(self):
        self.assertEqual(area(100), 10000)
        self.assertEqual(area(1000), 1000000)
        self.assertEqual(area(123), 15129)
    
    def test_area_return_type(self):
        self.assertIsInstance(area(3), (int, float))
        self.assertIsInstance(area(3.14), (int, float))
        self.assertIsInstance(area(-4), (int, float))
    
    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_positive_integer(self):
        self.assertEqual(perimeter(1), 4)
        self.assertEqual(perimeter(2), 8)
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10), 40)
    
    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(perimeter(1.5), 6.0)  
        self.assertAlmostEqual(perimeter(2.5), 10.0) 
        self.assertAlmostEqual(perimeter(0.25), 1.0)  
        self.assertAlmostEqual(perimeter(3.14159), 4 * 3.14159)
    
    def test_perimeter_negative_side(self):
        self.assertEqual(perimeter(-1), -4)
        self.assertEqual(perimeter(-2), -8)
        self.assertEqual(perimeter(-5), -20)
        self.assertAlmostEqual(perimeter(-1.5), -6.0)
    
    def test_perimeter_large_numbers(self):
        self.assertEqual(perimeter(100), 400)
        self.assertEqual(perimeter(1000), 4000)
        self.assertEqual(perimeter(123), 492)
    
    def test_perimeter_return_type(self):
        self.assertIsInstance(perimeter(3), (int, float))
        self.assertIsInstance(perimeter(3.14), (int, float))
        self.assertIsInstance(perimeter(-4), (int, float))
    
    def test_area_formula(self):
        for test_value in [1, 2, 3, 5, 10, 0.5, 1.5, 2.5]:
            with self.subTest(a=test_value):
                self.assertEqual(area(test_value), test_value * test_value)
    
    def test_perimeter_formula(self):
        for test_value in [1, 2, 3, 5, 10, 0.5, 1.5, 2.5]:
            with self.subTest(a=test_value):
                self.assertEqual(perimeter(test_value), 4 * test_value)
    
