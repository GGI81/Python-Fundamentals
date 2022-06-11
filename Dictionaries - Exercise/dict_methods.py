# Case Sensitive

# clear()
my_dict = {1: "apple", 2: "banana"}
my_dict.clear()
print(my_dict)  # {}

# copy()
my_dict = {1: "apple", 2: "banana"}
copied_dict = my_dict.copy()
print(my_dict == copied_dict)  # True

# pop()
a = {1: "1", 2: "2"}
a.pop(2)  # removes the key AND the VALUE
print(a)  # {1: "1"}

# popitem()
a = {1: "1", 2: "2", 3: "3"}
a.popitem()  # Removes the last Key AND the VALUE
print(a)  # {1: '1', 2: '2'}

# KEY WORD -> del
a = {1: "1", 2: "2", 3: "3"}
del a[3]
print(a)  # {1: '1', 2: '2'}

# get() (Save method)
my_dict = {1: "1", 2: "2"}
# print(my_dict[3])  ->  Key ERROR
print(my_dict.get(3))  # Returns None not ERROR

print()

my_dict = {"name": "jack", "age": 26}
print(my_dict["name"])
print(my_dict.get("name"))
