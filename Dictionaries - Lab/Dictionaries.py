# 1. Data Structures
# 2. Колекция от двойки
# 3. !!!Storing Key-Value Pairs!!!
# 4. Ordered collection
# 5. !!!Values can be of any data type and can repeat!!!
# 6. !!!Keys must be IMMUTABLE and must be UNIQUE!!!
# 7. Dictionaries don't have index

# Dict example
# my_dict = {"fruit": "apple", "vegetable": "cucumber"}
# Key  ->  #Value   |||   #Key   ->   #Value

my_dict = {"котка": "cat", "куче": "dog"}
people = {1: "Ivo Ivanov", 2: "Alex Georgiev"}


my_list = [200, 100, 50]
print(my_list[1])
print(my_dict["куче"])
print()
print()
print(people[2])


# !!!WE CANT PUT THE SAME KEYS IN ONE DICTIONARY!!!
# !!!IF ITS DONE, IT TAKES THE LAST ONE WITH THIS KEY NAME!!!

print()
print()
print()
print()
print()

# Second way to declare a dictionary:
# It is old and its not using anymore
# people = dict("name"="George", "age"=22)


# Adding a new Key - Value pair
people2 = {"name": "George", "age": 5}
people2["eyes color"] = "green"
print(people2)

print()
print()
print()
print()
print()

# New Build in function: -> zip()
keys = ["a", "b", "c"]
values = [1, 2, 3]

print(dict(zip(keys, values)))
print(dict(zip(values, keys)))

print()
print()
print()

# Making the same thing with for loop
keys = ["a", "b", "c"]
values = [1, 2, 3]

my_dict = {}

for index in range(len(keys)):
    my_dict[keys[index]] = values[index]
print(my_dict)

print()
print()
print()

# get function
my_dict = {1: "1", 2: "2"}

print(my_dict.get(3))  # None
# print(my_dict[3]) Breaking the program
print(my_dict.get(2))

print()
print()
print()

my_dict = {"a": "1", "b": "2"}
print(my_dict["a"])  # Case sensitive.  If it was "A" -> Error
print(my_dict.get("a"))  # Its not breaking. If it was "A" Returns -> None

print()
print()
print()

my_dict1 = {"a": "1", "b": "2"}
my_dict1["a"] = 5  # Update
my_dict1["z"] = 100  # Adds new Key - Value pair
print(my_dict1)

print()
print()
print()

my_dict = {}
my_dict1 = {"fruit": "apple", "Vegetable": "cucumber"}
print(type(my_dict))
print(my_dict1)

print()
print()
print()

# Hot to take something from the value when the value is a list
my_dict = {"a": ["Ines", "Georgi"], "b": ["Test1", "Test2"]}
print(my_dict["a"][1])  # Georgi

my_dict = {"a": ["Ines", "Georgi"], "b": ["Test1", "Test2"]}

names = my_dict["a"]
print(names[0])  # Ines

print()

# names becomes a list and we can use the list methods on it. It will give result to the value in the dictionary:
names = my_dict["a"]
names.append("Appended name")
print(my_dict)  # {'a': ['Ines', 'Georgi', 'Appended name'], 'b': ['Test1', 'Test2']}
