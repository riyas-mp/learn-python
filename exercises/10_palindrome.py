# This is a program that checks if a given string is a palindrome or not.
# eg: input: "level" output: True
# eg: input: "world" output: False
# eg: input: "madam" output: True
# eg: input: "python" output: False
# eg: input: "malayalam" output: True

text = input("Enter a word: ")
reversed_text = text[::-1]

if text == reversed_text:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
