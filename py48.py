list1 = [10, 20, 30, 40, 50]

list2 = list((1, 2, 3, 4, 5))

list3 = []
for i in range(1, 6):
    list3.append(i * 10)

print("List1:", list1)

print("List2 elements:")
for item in list2:
    print(item, end=" ")

print("\nSlicing List1:", list1[1:4])
