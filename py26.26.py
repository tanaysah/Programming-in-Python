test_str = "ABaBCbGc"

freq = {}

for ch in test_str:
    if ch not in freq:
        freq[ch] = 1
    else:
        freq[ch] = freq[ch] + 1

print("Count of all characters in ABaBCbGc is:\n", freq)
