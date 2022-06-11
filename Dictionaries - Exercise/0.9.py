command = input().split(" -> ")

my_dict = {}

while not command[0] == "End":
    company = command[0]
    employee_id = command[1]
    if company not in my_dict:
        my_dict[company] = []
        my_dict[company].append(employee_id)
    else:
        if employee_id not in my_dict[company]:
            my_dict[company].append(employee_id)
    command = input().split(" -> ")

my_dict = sorted(my_dict.items(), key=lambda x: (x[0], x[1]))

for key, value in my_dict:
    print(key)
    for j in value:
        print(f"-- {''.join(j)}")



"""
SoftUni -> AA12345
SoftUni -> BB12345
Microsoft -> CC12345
HP -> BB12345
End
"""
