string = input().split(" : ")

my_dict = {}

while string[0] != "end":
    course = string[0]
    name = string[1]
    if course not in my_dict:
        my_dict[course] = []
        my_dict[course].append(name)
    else:
        my_dict[course].append(name)
    string = input().split(" : ")

max_key = sorted(my_dict.items(), key=lambda x: (len(x[1])), reverse=True)
max_value = sorted(max_key, key=lambda x: (x[1]))
for course, student in max_key:
    print(f'{course}: {len(student)}')
    student = sorted(student)
    for el in student:
        print(f'-- {el}')