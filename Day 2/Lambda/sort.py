# Scenario 1: Sorting employees by performance score (descending)

employees = [("Asha", 85), ("Bala", 92), ("Chitra", 78)]

sorted_employees = sorted(employees, key=lambda x: x[1], reverse=True)

print("Employees sorted by performance (high to low):")
for emp in sorted_employees:
    print(emp[0], "->", emp[1])
