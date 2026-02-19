string = input("Enter main string: ")
substring = input("Enter substring: ")

count = 0

for i in range(len(string) - len(substring) + 1):
    match = True
    for j in range(len(substring)):
        if string[i + j] != substring[j]:
            match = False
            break
    if match:
        count += 1

print(count)
