word = input()
ind = []
for i in range(len(word)):
    if word[i].isupper():
        ind.append(i)
print(ind)