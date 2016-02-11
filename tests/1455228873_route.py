import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)).strip('tests'))
import unittest
from app.bin.application.Routes import Routes

class Testroute(unittest.TestCase):

    def test_init(self):
        routes = Routes()
        self.assertIsInstance(routes, Routes)


if __name__ == '__main__':
    print "route"
    unittest.main()
