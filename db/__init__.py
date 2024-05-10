from dotenv import load_dotenv
from db.employee import EmployeeController

load_dotenv()

employee_controller = EmployeeController()

print("123123")
print(employee_controller.get_employee_by_id(12))