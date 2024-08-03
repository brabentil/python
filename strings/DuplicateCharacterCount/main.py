def find_duplicate_characters(input_string):
    character_count = {}
    duplicates = []
    new_string=""

    for character in input_string:
        if character ==" ":
            continue
        else:
         new_string+=character


    for char in new_string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1


    for char, count in character_count.items():
        if count > 1:
            duplicates.append(char)

    return duplicates


input_string = input("Enter a string: ")
duplicates = find_duplicate_characters(input_string)
print(f"Duplicate characters: {', '.join(duplicates)}")
