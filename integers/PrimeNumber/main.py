def isprime(num):
    if num <= 1:
        return False

    for i in range(2, num // 2):
        if num % i == 0:
            return False

    return True


number = int(input("Enter a number: "))
if isprime(number):
    print("The number is prime")
else:
    print("The number is not prime")
