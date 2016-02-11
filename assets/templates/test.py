import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)).strip('tests'))
import unittest

class Test<_name_>(unittest.TestCase):

    def test_example(self):
        self.assertTrue(True)


if __name__ == '__main__':
    print "<_name_>"
    unittest.main()
