import logging
from db.db_helpers import db_connect as __db_connect__


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

            query_keys = ""
            query_values = ""

            # TODO(): Сделать перебор ключей и значений, для формирования готового выражения

            for key in user:
                if (bool(user[key])):
                    print(key, user[key])

            # print(bool(user.get("first_name")))

            # cursor.execute("INSERT INTO employees VALUES ()")

            # db_connection.commit()
        except Exception as e:
            db_connection.rollback()
            logging.error(msg=e)
        finally:
            cursor.close()
            db_connection.close()

    def edit_employee(self, id: int, first_name: str = None, last_name: str = None, ):
        try:
            db_connection = __db_connect__()
            cursor = db_connection.cursor()

            def ggg(param):
                if bool(param):
                    res = {}
                    res[param] = 0
                    print(res[param])

            ggg("first_name")
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