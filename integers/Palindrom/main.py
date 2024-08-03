def is_palindrome(num):
    return num == reversenum(num)


def reversenum(input):
    newnum = 0

    while input > 0:
        newnum = newnum * 10 + (input % 10)
        input = input // 10
    return newnum


num = int(input('Enter a number: '))

if is_palindrome(num):
    print('It is a palindrome')
else:
    print('It is not a palindrome')
