arr = [3, 7, 3, 5, 2, 5, 9, 2]
unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print(unique)
