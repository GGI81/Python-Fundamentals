current_year = int(input())

while True:
    current_year += 1
    current_year_as_string = str(current_year)
    happy_year = True
    for test_position in range(len(current_year_as_string)):
        test_digit = current_year_as_string[test_position]
        for current_position in range(len(current_year_as_string)):
            if test_digit == current_year_as_string[current_position] and not test_position == current_position:
                happy_year = False
                break
    if happy_year: # if happy_year == True
        print(current_year_as_string, end="")
        break