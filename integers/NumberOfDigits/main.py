num = int(input("Enter a number"))

numDigits = 0

while num > 0:
    numDigits += 1
    num //= 10

print('The number of digits is', numDigits)
