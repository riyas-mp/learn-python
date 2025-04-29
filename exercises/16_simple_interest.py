# This program calculates the simple interest for a given principal amount, interest rate, and time.
# Simple Interest formula: SI = (P * R * T) / 100
# where P = principal amount, R = rate of interest per year, T = time in years
# for example, if the principal amount is 1000, the rate of interest is 5% per year, and the time is 2 years,
# the simple interest would be (1000 * 5 * 2) / 100 = 100

principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate (% per year): "))
time = float(input("Enter time (in years): "))

simple_interest = (principal * rate * time) / 100
print(f"Simple Interest is {simple_interest}")
