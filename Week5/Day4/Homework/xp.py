# Create a function called get_words_from_file. 
# This function should read the file’s content and return the words as a collection. 
# What is the correct data type to store the words?
import random

def get_words_from_file():
    f = open('C:/Users/Fenriz/Desktop/DI/HTML/DI_Bootcamp/Week5/Day4/Homework/words.txt')
    text = f.read()
    f.close()
    text_list = text.split("\n")  #split function automatically returns a list. no need to make empty list beforehand
    return text_list


# Create another function called get_random_sentence which takes a single parameter called length. 
# The length parameter will be used to determine how many words the sentence should have. 
# The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), 
# the sentence should be lower case.

def get_random_sentence(length):
    sentence = ""
    text = get_words_from_file()
    for i in range(length):
        index_number = random.randint(0, len(text)-1)
        word_index = text[index_number].lower()
        sentence += word_index + " "
    print(sentence)


def main():
    print("This function takes a random user integer and then prints a sentence\n")
    try:
        user_number = int(input("Please pick a number between 2 and 20\n"))
        if user_number < 2 or user_number > 20:
            print("Error! Number should be between 2 and 20!")
            return
        get_random_sentence(user_number)
    except:
        print("Invalid Input!")

    
main()


