import unittest
from homework.tests_simple_employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Ihor', 'Piaskovskyi', 100)

    def tearDown(self):
        print("Tearing down!\n")

    def test_email(self):
        self.assertEqual(self.employee.email, 'Ihor.Piaskovskyi@email.com')

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, 'Ihor Piaskovskyi')

    def test_apply_raise(self):
        pass

    def test_monthly_schedule(self):
        pass


if __name__ == '__main__':
    unittest.main()
