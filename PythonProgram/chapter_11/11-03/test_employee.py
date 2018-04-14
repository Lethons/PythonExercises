import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('tom', 'jack', 4000)
        self.salay = [8000, 9000]

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.salay[1], self.my_employee.salary)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(4000)
        self.assertEqual(self.salay[0], self.my_employee.salary)


unittest.main()
