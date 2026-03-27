import unittest
# from ..src.python_flask_dev.filtering_data import get_filtered_key_vals
import sys


# class TestStringMethods(unittest.TestCase):

    # # Example test cases:
    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    # def test_get_filtered_key_vals(self):
    #     filtered_data = get_filtered_key_vals('id', filepath="/home/dani/Work/Work-Projects/sample-projects/python-flask-dev/src/data/users.json")
    #     result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #
    #     self.assertEqual(filtered_data, result)

if __name__ == '__main__':
    # unittest.main()
    print(sys.modules)
    for i in sys.modules.keys():
        if i == "python-flask-dev":
            print("module: ", sys.modules[i])