string_1 = input()
string_2 = input()
last_string = string_1

for symbol in range(len(string_1)):
    left_part = string_2[:symbol + 1]
    right_part = string_1[symbol + 1:]
    current_string = left_part + right_part
    if current_string == last_string:
        continue
    print(current_string)
    last_string = current_string


#!!!slicing -> [:3](0,1,2), [2:](3), [2:5]() chisloto 5 e stupka!!!