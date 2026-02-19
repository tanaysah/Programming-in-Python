text = input("Enter a string: ")
text = text.upper()

count = {}

for char in text:
    if char.isalpha():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

for key in sorted(count):
    print(count[key], key, sep="")
