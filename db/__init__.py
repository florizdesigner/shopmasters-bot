from dotenv import load_dotenv
from db.employee import EmployeeController

load_dotenv()

employee_controller = EmployeeController()

print(employee_controller.add_employee({"first_name": "Ivan", "last_name": "None"}))