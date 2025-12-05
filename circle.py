import math
import unittest


def area(r):
    '''
    принимает радиус r и возвращает площадь круга с радиусом r
    параметры: r (double)
    возвращает: площадь круга (double)
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    принимает радиус r и возвращает периметр круга с радиусом r
    параметры: r (double)
    возвращает: периметр круга (double)
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        self.assertEqual(area(0), 0)
    
    def test_area_positive_radius(self):
        self.assertAlmostEqual(area(1), math.pi)
        self.assertAlmostEqual(area(2), 4 * math.pi)
        self.assertAlmostEqual(area(10), 100 * math.pi)
    
    def test_area_return_type(self):
        self.assertIsInstance(area(1), (int, float))
    
    def test_perimeter_zero_radius(self):
        self.assertEqual(perimeter(0), 0)
    
    def test_perimeter_positive_radius(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)
        self.assertAlmostEqual(perimeter(7.5), 15 * math.pi)
    
    def test_perimeter_return_type(self):
        self.assertIsInstance(perimeter(3), (int, float))