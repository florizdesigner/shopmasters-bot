from dotenv import load_dotenv
from db.employee import EmployeeController
import logging

load_dotenv()
employee_controller = EmployeeController()

logging.basicConfig(filename="../logs/employees.log", filemode="w", format="[%(asctime)s] | [%(levelname)s] | %(message)s", level="INFO")
# print(employee_controller.add_employee({
#     "first_name": "Ivan",
#     "last_name": "Petrov",
#     "telegram_id": 123123123,
#     "telegram_username": "abobobboobob",
#     "is_fulltime": True,
#     "work_group": 1
# }))

result = employee_controller.edit_employee(12, {"telegram_id": 343434113, "telegram_username": "testtelegramusername220", "is_fulltime": False})
# print(employee_controller.delete_employee(28))

logging.info(msg=result)