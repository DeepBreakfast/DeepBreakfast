import unittest
import tests.testbisect
import tests.testExample

def suite():
    s = unittest.TestSuite()

    s.addTest(unittest.makeSuite(tests.testExample.TestSequenceFunctions))
    s.addTest(unittest.makeSuite(tests.testbisect.TestBisection))

    return s

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
