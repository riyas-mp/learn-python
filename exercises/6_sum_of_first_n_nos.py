n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
    total += i

print(f"Sum of first {n} numbers is {total}")

# The above code calculates the sum of the first `n` natural numbers using a `for` loop.
# The loop starts from `i = 1` and ends at `i = n`.
# In each iteration, it adds the current value of `i` to the `total` variable.
# Finally, it prints the total sum.

# range(1, n + 1) generates a sequence of numbers from `1` to `n`, inclusive.
# the 'f' string is used to format the output string, allowing for easy insertion of variables into the string.
# The `f` before the string indicates that it is an f-string, which allows for variable interpolation.
