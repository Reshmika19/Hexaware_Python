from enrollment import Enrollment

class Student:
    def __init__(self, name):
        self.name = name
        self.enrollment = Enrollment(self)

    def calculate_total_credits(self):
        return self.enrollment.calculate_total_credits()

    def calculate_fees(self):
        return self.enrollment.calculate_total_fees()


class PremiumStudent(Student):
    def calculate_fees(self):
        total = super().calculate_fees()
        return total * 0.8 
