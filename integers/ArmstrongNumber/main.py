num = int(input("Enter a number: "))
numCopy = num
i = 0
total = 0

while numCopy > 0:
    i += 1
    numCopy /= 10

numCopy = num

while numCopy > 0:
    total = total + (numCopy % 10) ** i
    numCopy /= 10

if total == num:
    print(num, "is an armstrong number")
else:
    print(num, 'is not an armstrong number')
