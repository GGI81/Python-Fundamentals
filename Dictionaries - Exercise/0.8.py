n = int(input())

my_dict = {}

for i in range(1, n + 1):
    name = input()
    grade = float(input())
    if name not in my_dict:
        my_dict[name] = []
    my_dict[name].append(grade)

my_dict = {s: sum(g) / len(g) for s, g in my_dict.items() if sum(g) / len(g) >= 4.50}

for key, value in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
    print(f"{key} -> {value:.2f}")

