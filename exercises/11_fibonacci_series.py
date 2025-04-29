# This is a fibonacci series program in Python
# It takes the number of terms as input and prints the Fibonacci series up to that number of terms
# Fibonacci series is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.
# The series starts as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Example: If the user inputs 10, the output will be: 0 1 1 2 3 5 8 13 21 34
# Example: If the user inputs 5, the output will be: 0 1 1 2 3

n = int(input("How many terms? "))

a, b = 0, 1
count = 0

while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
