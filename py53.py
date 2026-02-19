tuple1 = (10, 20, 30, 40, 50)

tuple2 = tuple([1, 2, 3, 4, 5])

print("Tuple1:", tuple1)

print("Tuple2 elements:")
for item in tuple2:
    print(item, end=" ")

print("\nSlicing Tuple1:", tuple1[1:4])

print("Count of 20:", tuple1.count(20))
print("Index of 30:", tuple1.index(30))

print("Maximum:", max(tuple1))
print("Minimum:", min(tuple1))
