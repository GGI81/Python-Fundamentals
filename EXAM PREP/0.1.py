employee1 = int(input())
employee2 = int(input())
employee3 = int(input())

people_count = int(input())

people_per_hour = employee1 + employee2 + employee3
hours = 0

while people_count > 0:
    hours += 1
    people_count -= people_per_hour

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")
