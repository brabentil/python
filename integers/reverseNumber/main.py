input_number = int(input("Enter a number: "))

def reverse_number(input_number):
    reversed_number = 0
    while input_number > 0:
        remainder = input_number % 10
        reversed_number = reversed_number*10 + remainder
        input_number = input_number//10
    return reversed_number

print(reverse_number(input_number))