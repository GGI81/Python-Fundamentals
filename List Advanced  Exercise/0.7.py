numbers = [int(i) for i in input().split(", ")]
step = 10
while numbers:
    my_list = []
    for i in numbers:
        if i <= step:
            my_list.append(i)
    for x in my_list:
        numbers.remove(x)
    print(f"Group of {step}'s: {my_list}")
    step += 10