import unittest

class TestSingleMethod(unittest.TestCase):

	def test_true(self):
		self.assertTrue(True)

	def test_false(self):
		self.assertFalse(False)

if __name__ == '__main__':
    print "test1"
    unittest.main()