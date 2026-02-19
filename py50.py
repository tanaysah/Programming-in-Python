numbers = [10, 20, 30, 20, 40]

numbers.append(50)
print("After append:", numbers)

numbers.insert(2, 25)
print("After insert:", numbers)

numbers.extend([60, 70])
print("After extend:", numbers)

print("Count of 20:", numbers.count(20))

numbers.remove(20)
print("After remove:", numbers)

numbers.pop()
print("After pop:", numbers)

numbers.sort()
print("After sort:", numbers)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
