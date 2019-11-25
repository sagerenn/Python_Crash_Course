import unittest
from employee import Employee

class TestEmpolyee(unittest.TestCase):
    """Test the employee.py"""

    def setUp(self):
        """create an instance to test"""
        self.susan = Employee('susan', 'z' , 10000)

    def test_give_default_raise(self):
        """Test increase the default raise salaray"""
        self.susan.give_raise()
        self.assertEqual(15000, self.susan.salary)

    def test_give_custom_raise(self):
        """Test increase the custom raise salaray"""
        self.susan.give_raise(7000)
        self.assertEqual(17000, self.susan.salary)

if __name__ == '__main__':
    unittest.main()