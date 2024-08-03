num = int(input("Enter a number: "))
newnum = num
sum = 0

while newnum > 0:
    digit = newnum % 10
    sum += digit
    newnum //= 10

print("The sum of the digits in ", num, " is", sum)
