from db.db_helpers import db_connect as __db_connect__
class EmployeeController:
    def get_all_employees(self):
        db_connection = __db_connect__()
        cursor = db_connection.cursor()

        try:
            cursor.execute("SELECT * FROM employees")
            return cursor.fetchall()
        except Exception as e:
            print(e)

    def get_employee_by_id(self, id: int):
        db_connection = __db_connect__()
        cursor = db_connection.cursor()

        try:
            cursor.execute(f"SELECT * FROM employees WHERE id = {id}")
            return cursor.fetchone()
        except Exception as e:
            print(e)

    def edit_employee(self):
        return