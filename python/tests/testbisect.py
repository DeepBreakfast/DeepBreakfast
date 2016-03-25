import unittest
import bisect 
import math

class TestBisection(unittest.TestCase):
    def setUp(self):
        pass 

    def tearDown(self):
        pass

    def test_bisection(self):
        def f(x): 
            return x 
        def g(x):
            return x*x-2 
        def h(x): 
            return 1 
        expected = 0 
        actual = bisect.bisection(f,-1,2,1e-10)
        self.assertAlmostEqual(expected,actual)

        expected = math.sqrt(2)
        actual = bisect.bisection(g,-1,2,1e-10)
        self.assertAlmostEqual(expected,actual)

        self.assertIsNone(bisect.bisection(h,-1,2))

