nums = [int(el) for el in input().split()]
factor = int(input())

happines = [el * factor for el in nums]
threshold = sum(happines) / len(happines)

happy_eployees = [el for el in happines if el >= threshold]
sad_eployees = [el for el in happines if el < threshold]

happy_message = "Employees are happy!"
sad_massage = "Employees are not happy!"

if len(sad_eployees) > len(happines) / 2:
    print(f"Score: {len(happy_eployees)}/{len(happines)}. {sad_massage}")
else:
    print(f"Score: {len(happy_eployees)}/{len(happines)}. {happy_message}")