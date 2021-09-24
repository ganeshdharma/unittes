import unittest
import main
class TestMain(unittest.TestCase):
    def test_do_stuff1(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
    def test_do_stuff2(self):
        test_param = 'hsdsh'
        result = main.do_stuff(test_param)
        self.assertEqual(result, ValueError)
    def test_do_stuff3(self):
        test_param = 'jndsj'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

unittest.main()

