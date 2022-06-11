employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
students_count = int(input())

answered_students_per_hour = employee1 + employee2 + employee3
hours = 0

while students_count > 0:
    students_count -= answered_students_per_hour
    hours += 1

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")

