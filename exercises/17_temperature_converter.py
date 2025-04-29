# This program converts temperature from Celsius to Fahrenheit.
# The formula to convert Celsius to Fahrenheit is: (C * 9/5) + 32
# 9/5 is the same as 1.8, so you could also use that in the formula.
# Adding 32 to the result of (C * 9/5) gives you the Fahrenheit equivalent.

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is {fahrenheit}°F")
