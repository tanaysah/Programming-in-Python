def format_name(full_name):
    words = full_name.split()
    result = ""

    for i in range(len(words) - 1):
        result += words[i][0].upper() + "."

    result += " " + words[-1].capitalize()
    return result

s = "mohandas karamchand gandhi"
print(format_name(s))
