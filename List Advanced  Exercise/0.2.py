input_version = [int(i) for i in input().split(".")]

for i in input_version:
    if input_version[2] == 9 and input_version[1] < 9:
        input_version[2] = 0
        input_version[1] += 1
        break
    elif input_version[2] and input_version[1] == 9:
        input_version[2] = 0
        input_version[1] = 0
        input_version[0] += 1
        break
    elif input_version[0] > 9:
        break
    else:
        input_version[2] += 1
        break
print(".".join(map(str, input_version)))


"""
version = input().split(", ")
version_string = ''.join(version)

version_num = int(version_string)
version_num += 1

next_version_string = str(version_num)
next_version = list(next_version_string)

print(f'{".".join(next_version)}')
"""