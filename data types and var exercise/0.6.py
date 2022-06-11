number = int(input())

for i in range(0, number):  #0,1,2,3,
    for k in range(0, number):
        for j in range(0, number):
            print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}")
            #000
            #001
            #002
            #010
            #011
            #012
            #020
            #021
            #022
            #100
            #101
            #102
