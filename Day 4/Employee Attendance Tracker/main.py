'''
Employee Attendance Tracker

Problem Statement:
You are creating an Employee Attendance Tracker for a company. Employees can check in and
check out, and the system tracks total hours worked. All data is stored in a SQL database.
'''


from employeeAttendance import EmployeeAttendanceDB
from datetime import datetime

def main():
    db = EmployeeAttendanceDB()

    while True:
        print("\n=== Employee Attendance Tracker ===")
        print("1. Add Employee")
        print("2. Check-In")
        print("3. Check-Out")
        print("4. Generate Attendance Report")
        print("5. List Incomplete Attendance")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter employee name: ")
            department = input("Enter department: ")
            db.add_employee(name, department)

        elif choice == "2":
            emp_id = int(input("Enter employee ID: "))
            db.check_in(emp_id)

        elif choice == "3":
            emp_id = int(input("Enter employee ID: "))
            db.check_out(emp_id)

        elif choice == "4":
            emp_id_input = input("Enter employee ID (or press Enter for all): ")
            emp_id = int(emp_id_input) if emp_id_input.strip() else None

            date_filter = input("Do you want to filter by date range? (y/n): ")
            if date_filter.lower() == "y":
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                db.generate_report(emp_id, start_date, end_date)
            else:
                db.generate_report(emp_id)

        elif choice == "5":
            db.list_incomplete_attendance()

        elif choice == "6":
            print("Exiting Employee Attendance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
