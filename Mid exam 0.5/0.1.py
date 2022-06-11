import math
import sys

students = int(input())
lectures = int(input())
bonus = int(input())

total_bonus = 0
max_bonus = -sys.maxsize
best_student = -sys.maxsize
for i in range(students):
    follow_attendances = int(input())
    total_bonus = math.ceil((follow_attendances / lectures) * (5 + bonus))
    if lectures == 0:
        print(f'Max Bonus: 0.')
        print(f'The student has attended 0 lectures.')
    if max_bonus <= total_bonus:
        max_bonus = total_bonus
    if best_student <= follow_attendances:
        best_student = follow_attendances
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {best_student} lectures.")

                    # 90 / 100
