path = input().split("\\")

list_text = []
for text in path:
    for ch in text:
        if ch == ".":
            fine_name_extract = text
            list_text = fine_name_extract.split(".")
print(f"File name: {list_text[0]}")
print(f"File extension: {list_text[1]}")


# string = input().split("\\")
#
# subtract = string[2]
# f_n_extension = string[3]
# data = f_n_extension.split(".")
# file_name = data[0]
# extension = data[1]
#
# print(f"File name: {file_name}")
# print(f"File extension: {extension}")
