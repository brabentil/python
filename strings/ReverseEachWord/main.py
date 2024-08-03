def reverseWord(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return reversed_word


def reverseEachWord(sentence):
    array = sentence.split(" ")
    reversed_array = []

    for word in array:
        reversed_word = reverseWord(word)
        reversed_array.append(reversed_word)

    return " ".join(reversed_array)


inputString = input("Enter a sentence: ")
print(reverseEachWord(inputString))
