def function(num1, num2, num3):
    my_list = [num1, num2, num3]
    negatives = 0
    for i in range(len(my_list)):
        if "-" in my_list[i]:
            negatives += 1
    if negatives % 2 != 0:
        print("negative")
    elif "0" in my_list:
        print("zero")
    else:
        print("positive")


num1_input = input()
num2_input = input()
num3_input = input()

function(num1_input, num2_input, num3_input)