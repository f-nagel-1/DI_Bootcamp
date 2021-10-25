# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# Then, print the first and last characters of the given text.

user_input = input("please give me a 10 letter word\n")

while len(user_input) < 10 or len(user_input) > 10:
    if len(user_input) < 10:
        print("too short")
    elif len(user_input) > 10:
        print("too long")
    else:
        print("this is the first letter of your word:\n", user_input[0], "\n and this is the last letter of your word:\n", user_input[-1])


# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World


i = 0
while i < len(user_input):
    i += 1
    print (user_input[0:i])
    

# //exercise 3

import random
scrambled = list(user_input)
random.shuffle(scrambled)
print("".join(scrambled))