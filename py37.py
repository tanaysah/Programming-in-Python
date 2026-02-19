full_name = input("Enter full name: ")
names = full_name.split()

first = names[0]
middle = names[1]
last = names[2]

print(first[0].upper() + "." + middle[0].upper() + ". " + last.capitalize())
