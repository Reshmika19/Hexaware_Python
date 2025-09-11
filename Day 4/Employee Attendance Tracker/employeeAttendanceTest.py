import inspect
from employeeAttendance import EmployeeAttendanceDB   

def test_add_employee_query():
    db = EmployeeAttendanceDB()
    expected_query = "INSERT INTO employees (name, department) VALUES (%s, %s)"
    actual_query = inspect.getsource(db.add_employee)
    assert expected_query in actual_query

def test_check_in_query():
    db = EmployeeAttendanceDB()
    expected_query = "INSERT INTO attendance (employee_id, check_in) VALUES (%s, %s)"
    actual_query = inspect.getsource(db.check_in)
    assert expected_query in actual_query

def test_check_out_query():
    db = EmployeeAttendanceDB()
    expected_query = "UPDATE attendance \n                SET check_out = %s, total_hours = %s \n                WHERE attendance_id = %s"
    actual_query = inspect.getsource(db.check_out)
    assert expected_query in actual_query

def test_generate_report_query():
    db = EmployeeAttendanceDB()
    expected_query = "SELECT e.name, e.department, a.check_in, a.check_out, a.total_hours"
    actual_query = inspect.getsource(db.generate_report)
    assert expected_query in actual_query

def test_list_incomplete_attendance_query():
    db = EmployeeAttendanceDB()
    expected_query = "SELECT e.employee_id, e.name, e.department, a.check_in"
    actual_query = inspect.getsource(db.list_incomplete_attendance)
    assert expected_query in actual_query