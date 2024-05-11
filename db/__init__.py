from dotenv import load_dotenv
from db.employee import EmployeeController

load_dotenv()
employee_controller = EmployeeController()

# print(employee_controller.add_employee({
#     "first_name": "Ivan",
#     "last_name": "Petrov",
#     "telegram_id": 123123123,
#     "telegram_username": "abobobboobob",
#     "is_fulltime": True,
#     "work_group": 1
# }))

print(employee_controller.edit_employee(12, {"telegram_id": 343434333, "telegram_username": "testtelegramusername123"}))