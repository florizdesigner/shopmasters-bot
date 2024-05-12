import logging
from db.db_helpers import db_connect as __db_connect__
from models.DBResponse import DBResponse
from models.Employee import Employee


class EmployeeController:
    # настройка формата логирования
    logging.basicConfig(filename="../logs/employees.log", filemode="w", format="[%(asctime)s] | [%(levelname)s] | %(message)s", level="INFO")

    def get_all_employees(self):
        try:
            db_connection = __db_connect__()
            cursor = db_connection.cursor()

            logging.info(msg=f"Started search all employees")
            cursor.execute("SELECT * FROM employees")
            result = cursor.fetchall()
            logging.info(msg=f"Success! Result: {result}")
        except Exception as e:
            logging.error(msg=e)
        finally:
            cursor.close()
            db_connection.close()

    def get_employee_by_id(self, id: int):
        try:
            db_connection = __db_connect__()
            cursor = db_connection.cursor()
            logging.info(msg=f"Started search employee by id: {id}")

            cursor.execute(f"SELECT * FROM employees WHERE id = {id}")
            result = cursor.fetchone()
            logging.info(msg=f"Employee: {result}")
            return result
        except Exception as e:
            logging.error(msg=e)
        finally:
            cursor.close()
            db_connection.close()

    def add_employee(self, user: object):
        try:
            db_connection = __db_connect__()
            cursor = db_connection.cursor()

            user = Employee.from_dict(user).to_dict()

            logging.info(msg=f"Request to add user: {user}")
            cursor.execute(f"INSERT INTO employees (first_name, last_name, telegram_id, telegram_username, is_fulltime, work_group, type_of_fulltime_shifts, is_absence) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                           (user["first_name"], user['last_name'], user['telegram_id'], user['telegram_username'], user['is_fulltime'], user['work_group'], user['type_of_fulltime_shifts'], user['is_absence']))
            db_connection.commit()
            logging.info(msg="User successfully added!")
        except Exception as e:
            db_connection.rollback()
            logging.error(msg=e)
        finally:
            cursor.close()
            db_connection.close()

    def edit_employee(self, id: int, params: object):
        try:
            logging.info(msg=f"Incoming request to edit employee. Parameters: {str(params)}, ID: {id}")
            db_connection = __db_connect__()
            cursor = db_connection.cursor()

            cursor.execute(f"select * from employees where id = {id}")
            employee = Employee(*cursor.fetchone()[1:]).to_dict()

            for parameter in params:
                employee[parameter] = params[parameter]

            employee_str = ""
            tuple_employee = tuple(employee)

            for index, ele in enumerate(tuple_employee):
                if index != len(tuple_employee) - 1:
                    employee_str += str(ele) + ', '
                else:
                    employee_str += str(ele)

            print(f"update employees set ({employee_str}) = {tuple(employee.values())} where id = {id}")

            cursor.execute(f"update employees set ({employee_str}) = {tuple(employee.values())} where id = {id}")

            db_connection.commit()

            cursor.execute(f"select * from employees where id = {id}")
            updated_employee = Employee(*cursor.fetchone()[1:]).to_dict()

            return DBResponse(status="success", message="User successfull edited", employee=updated_employee)

        except Exception as e:
            db_connection.rollback()
            logging.error(msg=e)
        finally:
            cursor.close()
            db_connection.close()


    def delete_employee(self, id: int):
        try:
            logging.info(msg=f"Incoming request to delete user. UserID: {id}")
            db_connection = __db_connect__()
            cursor = db_connection.cursor()

            cursor.execute(f"DELETE FROM employees WHERE id = {id}")
            db_connection.commit()

            response = DBResponse(status="success", message=f"User id: {id} is successfully deleted from DB").to_dict()
            logging.info(msg=response)

            return response
        except Exception as e:
            db_connection.rollback()
            logging.error(msg=e)
        finally:
            cursor.close()
            db_connection.close()