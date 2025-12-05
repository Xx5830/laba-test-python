import math
import unittest

def area(a, h): 
    '''
    принимает a, h (double) возвращает площадь треугольника со стороной a и высотой h
    параметры: a, h (double)
    возвращает: площадь треугольника (double)
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    принимает a, b, c (double) возвращает периметр треугольника со сторонами a, b, c
    параметры: a, b, c (double)
    возвращает: периметр треугольника (double)
    '''
    return a + b + c 

class TriangleTestCase(unittest.TestCase):
    def test_area_zero_base_or_height(self):
        self.assertEqual(area(0, 5), 0)     
        self.assertEqual(area(5, 0), 0)      
        self.assertEqual(area(0, 0), 0)      
    
    def test_area_positive_integers(self):
        self.assertEqual(area(1, 1), 0.5)   
        self.assertEqual(area(2, 3), 3)      
        self.assertEqual(area(4, 6), 12)     
        self.assertEqual(area(10, 5), 25)   
    
    def test_area_positive_floats(self):
        self.assertAlmostEqual(area(1.5, 2), 1.5)    
        self.assertAlmostEqual(area(3.5, 4.2), 7.35) 
        self.assertAlmostEqual(area(0.5, 0.8), 0.2)  
    
    def test_area_negative_values(self):
        self.assertEqual(area(-1, 5), -2.5)    
        self.assertEqual(area(3, -4), -6)        
        self.assertEqual(area(-2, -3), 3)        
    
    def test_area_large_numbers(self):
        self.assertEqual(area(100, 50), 2500)    
        self.assertEqual(area(1000, 1000), 500000) 
    
    def test_area_return_type(self):
        self.assertIsInstance(area(3, 4), (int, float))
        self.assertIsInstance(area(3.5, 4.2), (int, float))
    
    def test_perimeter_zero_sides(self):
        self.assertEqual(perimeter(0, 0, 0), 0)          
        self.assertEqual(perimeter(0, 5, 7), 12)          
        self.assertEqual(perimeter(3, 0, 4), 7)           
        self.assertEqual(perimeter(2, 3, 0), 5)           
    
    def test_perimeter_positive_integers(self):
        self.assertEqual(perimeter(1, 1, 1), 3)        
        self.assertEqual(perimeter(3, 4, 5), 12)          
        self.assertEqual(perimeter(5, 7, 9), 21)
        self.assertEqual(perimeter(10, 20, 30), 60)
    
    def test_perimeter_positive_floats(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3.5), 7.5)  
        self.assertAlmostEqual(perimeter(0.2, 0.3, 0.4), 0.9)  
        self.assertAlmostEqual(perimeter(3.14, 2.71, 4.20), 10.05)
    
    def test_perimeter_negative_values(self):
        self.assertEqual(perimeter(-1, 2, 3), 4)          
        self.assertEqual(perimeter(1, -2, 3), 2)         
        self.assertEqual(perimeter(-1, -2, -3), -6)       
        self.assertEqual(perimeter(-1.5, 2.5, -1), 0)     
    
    def test_perimeter_large_numbers(self):
        self.assertEqual(perimeter(100, 100, 100), 300)
        self.assertEqual(perimeter(1000, 2000, 3000), 6000)
    
    def test_perimeter_return_type(self):
        self.assertIsInstance(perimeter(3, 4, 5), (int, float))
        self.assertIsInstance(perimeter(3.5, 4.2, 5.1), (int, float))
    
    def test_perimeter_commutative(self):
        self.assertEqual(perimeter(3, 4, 5), perimeter(5, 4, 3))
        self.assertEqual(perimeter(3, 4, 5), perimeter(4, 5, 3))
        self.assertEqual(perimeter(7, 8, 9), perimeter(9, 7, 8))
    
    def test_area_formula(self):
        test_cases = [
            (2, 3),    
            (4, 5),    
            (1.5, 2),  
            (3.5, 4.2) 
        ]
        for a, h in test_cases:
            with self.subTest(a=a, h=h):
                expected = a * h / 2
                self.assertAlmostEqual(area(a, h), expected)
    
    def test_perimeter_formula(self):
        test_cases = [
            (3, 4, 5),      
            (7, 8, 9),      
            (1.5, 2.5, 3.5) 
        ]
        for a, b, c in test_cases:
            with self.subTest(a=a, b=b, c=c):
                expected = a + b + c
                self.assertAlmostEqual(perimeter(a, b, c), expected)
    
    def test_area_floating_point_precision(self):
        self.assertAlmostEqual(area(0.0001, 0.0002), 0.00000001)
        self.assertAlmostEqual(area(1000000, 0.000001), 0.5)
    
    def test_perimeter_floating_point_precision(self):
        self.assertAlmostEqual(perimeter(0.1, 0.2, 0.3), 0.6)
        self.assertAlmostEqual(perimeter(1e-9, 2e-9, 3e-9), 6e-9)
