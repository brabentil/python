def characterCounter(input):
    charCount = {}
    for char in input:
        if char not in charCount:
            charCount[char] = 1
        else:
            charCount[char] += 1
    return charCount


input_string = input("Enter a string: ")
char_count = characterCounter(input_string)

print("Character Count:")
for char, count in char_count.items():
    print(f"'{char}': {count}")
