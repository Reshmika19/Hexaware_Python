# Scenario 5: Sorting students by marks using lambda

students = {"Asha": 78, "Bala": 90, "Chitra": 65}

rank_list = sorted(students.items(), key=lambda x: x[1], reverse=True)

print("Rank List:")
for i, (name, mark) in enumerate(rank_list, start=1):
    print(f"{i}. {name} -> {mark}")
