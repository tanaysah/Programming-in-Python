text = input("Enter a string: ")

print("Forward order:")
for i in range(len(text)):
    print(text[i], end="")

print("\nReverse order:")
for i in range(len(text)-1, -1, -1):
    print(text[i], end="")
