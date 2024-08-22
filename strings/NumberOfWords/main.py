def numwords(text):

    text = text.strip()

    if not text:
        return 0

    words = text.split()

    return len(words)


text = input("Enter a text: ")

print(f'The number of words in "{text}" is {numwords(text)}')
