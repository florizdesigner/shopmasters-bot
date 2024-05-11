import logging
from db.db_helpers import db_connect as __db_connect__
from models.Employee import Employee


class EmployeeController:
    # настройка формата логирования
    logging.basicConfig(filename="../logs/employees_controller.log", filemode="w", format="[%(asctime)s] | [%(levelname)s] | %(message)s", level="INFO")

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
            db_connection = __db_connect__()
            cursor = db_connection.cursor()

            cursor.execute(f"select * from employees where id = {id}")
            employee = Employee(*cursor.fetchone()[1:])
            print(employee)

            # TODO(): Прогнать каждый переданный параметр и заменить на новые данные в Employee

            for parameter in params:

                print(parameter, params[parameter])

            # cursor.execute(f"UPDATE employees SET first_name = {bool(first_name) if 'first_name' = first_name}")

        except Exception as e:
            db_connection.rollback()
            logging.error(msg=e)
        finally:
            cursor.close()
            db_connection.close()


    def delete_employee(self, id: int):
        try:
            db_connection = __db_connect__()
            cursor = db_connection.cursor()

            cursor.execute(f"DELETE FROM employees WHERE id = {id}")
            result = cursor.fetchone()
            print(result)

            db_connection.commit()
        except Exception as e:
            db_connection.rollback()
            logging.error(msg=e)
        finally:
            cursor.close()
            db_connection.close()