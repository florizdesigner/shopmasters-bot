import unittest

from db import EmployeeController
from models.DBResponse import DBResponse
from models.Employee import EmployeeRequest, EmployeeResponse


class DataBaseTest(unittest.TestCase):
    def setUp(self):
        self.employee_controller = EmployeeController()

    def test_create_employee(self):
        test_employee = EmployeeRequest(first_name="Auto1", last_name="Testov1", telegram_id=12313000,
                                        telegram_username="autotest_1", is_fulltime=True, work_group=1,
                                        type_of_fulltime_shifts=2, is_absence=False)
        create_employee_response = self.employee_controller.add_employee(test_employee)
        print(create_employee_response)
        self.assertEqual(create_employee_response.status,
                         "success",
                         "Test failed")

        self.assertIs(create_employee_response, DBResponse, "Type of response is wrong")
        self.assertEqual(create_employee_response.employee, EmployeeResponse, "Type of employee is wrong")


if __name__ == '__main__':
    unittest.main()
