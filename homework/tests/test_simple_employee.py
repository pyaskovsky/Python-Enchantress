import unittest
from homework.tests_simple_employee import Employee
from homework.tests import utils
from unittest import mock


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Ihor', 'Piaskovskyi', 56000)

    def test_email(self):
        self.assertEqual(self.employee.email, 'Ihor.Piaskovskyi@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, 'Ihor Piaskovskyi')

    def test_apply_raise(self):
        self.employee.apply_raise()
        self.assertEqual(self.employee.pay, 58800)

    @mock.patch("homework.tests.utils.make_request", return_value=True)
    def test_monthly_schedule(self, month):
        response = utils.parse_response(self.employee.last, 3)
        self.assertEqual(response, "Successful request")


if __name__ == '__main__':
    unittest.main()
