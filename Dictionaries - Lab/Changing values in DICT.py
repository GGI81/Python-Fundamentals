# Mutable collection
# IF THE KEY EXIST


may_dict = {"a": "1", "b": "2"}
may_dict["a"] = 5  # IF the key exist its changing its value
may_dict["z"] = 100  # IF it doesn't, it adds it into the dict
print(may_dict)
