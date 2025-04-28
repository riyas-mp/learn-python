# This is a password checker program that checks if the user input matches a predefined password.
# The program prompts the user to enter a password and checks if it matches the stored password.

password = "secret123"
user_input = input("Enter the password: ")

if user_input == password:
    print("Access Granted!")
else:
    print("Access Denied!")
