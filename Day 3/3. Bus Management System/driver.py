class Driver:
    def __init__(self, name, employee_id, license_number):
        self.name = name
        self.employee_id = employee_id
        self.license_number = license_number

    def display_details(self):
        print(f"Driver: {self.name}, ID: {self.employee_id}, License: {self.license_number}")
