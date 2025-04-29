# This is a program that calculates the factorial of a given number.
# The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n.
# For example, 5! = 5 * 4 * 3 * 2 * 1 = 120.
# The factorial of 0 is defined to be 1.

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")
