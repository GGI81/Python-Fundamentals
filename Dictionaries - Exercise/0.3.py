countries = input().split(", ")
capital_city = input().split(", ")

my_dict = {}

for i in range(len(countries)):
    my_dict[countries[i]] = capital_city[i]

for key, value in my_dict.items():
    print(f"{key} -> {value}")


"""
# The same result
# Using zip() build in function
countries2 = input()
capitals2 = input()

country_capital_info = dict(zip(countries2, capitals2))

for key, value in country_capital_info.items():
    print(f"{key} -> {value}")
"""