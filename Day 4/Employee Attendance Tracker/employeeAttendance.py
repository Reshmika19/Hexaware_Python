from config import get_connection
from mysql.connector import Error
from datetime import datetime

class EmployeeAttendanceDB:
    def add_employee(self, name, department):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO employees (name, department) VALUES (%s, %s)",
                (name, department)
            )
            conn.commit()
            print(f"Employee {name} added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def check_in(self, employee_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT * FROM attendance 
                WHERE employee_id = %s AND check_out IS NULL
            """, (employee_id,))
            if cursor.fetchone():
                print("Error: Employee already checked in without checkout.")
                return

            check_in_time = datetime.now()
            cursor.execute(
                "INSERT INTO attendance (employee_id, check_in) VALUES (%s, %s)",
                (employee_id, check_in_time)
            )
            conn.commit()
            print(f"Employee {employee_id} checked in at {check_in_time}.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def check_out(self, employee_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                SELECT attendance_id, check_in FROM attendance 
                WHERE employee_id = %s AND check_out IS NULL
            """, (employee_id,))
            record = cursor.fetchone()

            if not record:
                print("Error: No active check-in found.")
                return

            attendance_id, check_in_time = record
            check_out_time = datetime.now()
            total_hours = (check_out_time - check_in_time).total_seconds() / 3600.0

            cursor.execute("""
                UPDATE attendance 
                SET check_out = %s, total_hours = %s 
                WHERE attendance_id = %s
            """, (check_out_time, total_hours, attendance_id))

            conn.commit()
            print(f"Employee {employee_id} checked out at {check_out_time}. Hours worked: {total_hours:.2f}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def generate_report(self, employee_id=None, start_date=None, end_date=None):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            query = """
                SELECT e.name, e.department, a.check_in, a.check_out, a.total_hours
                FROM employees e
                JOIN attendance a ON e.employee_id = a.employee_id
                WHERE 1=1
            """
            params = []

            if employee_id:
                query += " AND e.employee_id = %s"
                params.append(employee_id)
            if start_date and end_date:
                query += " AND DATE(a.check_in) BETWEEN %s AND %s"
                params.extend([start_date, end_date])

            cursor.execute(query, tuple(params))
            rows = cursor.fetchall()

            print("Attendance Report:")
            for row in rows:
                print(row)

        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

    def list_incomplete_attendance(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT e.employee_id, e.name, e.department, a.check_in 
                FROM employees e 
                JOIN attendance a ON e.employee_id = a.employee_id 
                WHERE a.check_out IS NULL
            """)
            rows = cursor.fetchall()
            print("Employees with incomplete attendance:")
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()
