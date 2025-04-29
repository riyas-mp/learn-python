# This program checks if a given number is prime or not.
# A prime number is a number that is only divisible by 1 and itself.
# For example, 5 is a prime number because it is only divisible by 1 and 5.

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
