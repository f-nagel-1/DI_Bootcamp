# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# #For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher, the user entries the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.


# x = range(97,123)
# for number in x:
#     print(number)
# lower_case_range = range(97,123)



cypher_text = ""
process = input("Do you want to encrypt or decrypt?\n")

lower_accept_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

upper_accept_letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


if process.lower() == "encrypt":
    text_user = input("Please enter your text\n")
    for letter in text_user:
        if letter in lower_accept_letter:
            if letter == "x":
                cypher_text += "a"
            elif letter == "y":
                cypher_text += "b"
            elif letter == "z":
                cypher_text += "c"
            else:
                cypher_text += chr(ord(letter) + 3)

        elif letter in upper_accept_letter:
            if letter == "X":
                cypher_text += "A"
            elif letter == "Y":
                cypher_text += "B"
            elif letter == "Z":
                cypher_text += "C"
            else:
                cypher_text += chr(ord(letter) + 3)

        else:
            cypher_text += letter
    print(cypher_text)

elif process.lower() == "decrypt":
    text_user = input("Please enter your text\n")
    for letter in text_user:
        if letter in lower_accept_letter:
            if letter == "a":
                cypher_text += "x"
            elif letter == "b":
                cypher_text += "y"
            elif letter == "c":
                cypher_text += "z"
            else:
                cypher_text += chr(ord(letter) - 3)

        elif letter in upper_accept_letter:
            if letter == "A":
                cypher_text += "X"
            elif letter == "B":
                cypher_text += "Y"
            elif letter == "C":
                cypher_text += "Z"
            else:
                cypher_text += chr(ord(letter) - 3)

        else:
            cypher_text += letter

    print(cypher_text)



else:
    print("Error! Please enter valid choice")