def palindrome(sequence):
    for element in range(len(sequence)):
        backwards_number = ''.join(reversed(sequence[element]))
        if sequence[element] == backwards_number:
            print("True")
        else:
            print("False")


palindrome(input().split(", "))