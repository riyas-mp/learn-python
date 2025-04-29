# This program calculates the sum of digits of a given number.
# The sum of digits of a number is the sum of its individual digits.
# For example, the sum of digits of 1234 is 1 + 2 + 3 + 4 = 10.

# explanation:
# 1. The program prompts the user to enter a number.
# 2. The number is divided by 10 repeatedly until it becomes 0.
# 3. The sum of digits is calculated by adding the remainder of each division to the sum_digits variable.
# 4. Finally, the program prints the sum of digits.

number = int(input("Enter a number: "))
sum_digits = 0

while number > 0:
    sum_digits += number % 10
    number //= 10

print(f"Sum of digits is {sum_digits}")
