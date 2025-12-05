import math
import unittest

def area(a, b): 
    '''
    принимает a, b (double) возвращает площадь прямоугольника со сторонами a, b
    параметры: a, b (double)
    возвращает: площадь прямоугольника (double)
    '''
    return a * b 

def perimeter(a, b): 
    '''
    принимает a, b (double) возвращает периметр прямоугольника со сторонами a, b
    параметры: a, b (double)
    возвращает: периметр прямоугольника (double)
    '''
    return a + b 


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

    def test_area_zero_sides(self):
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(5, 0), 0)
        self.assertEqual(area(0, 3), 0)
    
    def test_area_positive_sides(self):
        self.assertEqual(area(1, 1), 1)
        self.assertEqual(area(2, 3), 6)
        self.assertEqual(area(5, 7), 35)
        self.assertEqual(area(10, 20), 200)
    
    def test_area_float_sides(self):
        self.assertAlmostEqual(area(1.5, 2), 3.0)
        self.assertAlmostEqual(area(2.5, 3.5), 8.75)
        self.assertAlmostEqual(area(0.1, 0.2), 0.02)
    
    def test_area_negative_sides(self):
        self.assertEqual(area(-1, 5), -5)
        self.assertEqual(area(3, -4), -12)
        self.assertEqual(area(-2, -3), 6)
    
    def test_area_return_type(self):
        self.assertIsInstance(area(1, 2), (int, float))
        self.assertIsInstance(area(1.5, 2.5), (int, float))
    
    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(5, 0), 10)  
        self.assertEqual(perimeter(0, 3), 6)   
    
    def test_perimeter_positive_sides(self):
        self.assertEqual(perimeter(1, 1), 4)    
        self.assertEqual(perimeter(2, 3), 10)   
        self.assertEqual(perimeter(5, 7), 24)   
        self.assertEqual(perimeter(10, 20), 60) 
    
    def test_perimeter_float_sides(self):
        self.assertAlmostEqual(perimeter(1.5, 2), 7.0)     
        self.assertAlmostEqual(perimeter(2.5, 3.5), 12.0)  
        self.assertAlmostEqual(perimeter(0.1, 0.2), 0.6)   
    
    def test_perimeter_negative_sides(self):
        self.assertEqual(perimeter(-1, 5), 8)     
        self.assertEqual(perimeter(3, -4), -2)    
        self.assertEqual(perimeter(-2, -3), -10)  
    
    def test_perimeter_return_type(self):
        self.assertIsInstance(perimeter(1, 2), (int, float))
        self.assertIsInstance(perimeter(1.5, 2.5), (int, float))
    
    def test_area_commutative(self):
        self.assertEqual(area(3, 4), area(4, 3))
        self.assertEqual(area(7, 2), area(2, 7))
    
    def test_perimeter_commutative(self):
        self.assertEqual(perimeter(3, 4), perimeter(4, 3))
        self.assertEqual(perimeter(7, 2), perimeter(2, 7))
    
    def test_area_large_numbers(self):
        self.assertEqual(area(1000, 1000), 1000000)
        self.assertEqual(area(999, 999), 998001)
    
    def test_perimeter_large_numbers(self):
        self.assertEqual(perimeter(1000, 1000), 4000)
        self.assertEqual(perimeter(999, 999), 3996)
