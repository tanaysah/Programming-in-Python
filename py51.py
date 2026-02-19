listA = [1, 2, 3, 4, 5]
listB = [4, 5, 6, 7, 8]

common = []

for item in listA:
    if item in listB:
        common.append(item)

print("Common elements:", common)
