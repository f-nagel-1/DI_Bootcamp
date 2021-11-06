from collections import Counter

def get_text_from_file():
    f = open('C:/Users/Fenriz/Desktop/DI/HTML/DI_Bootcamp/Week5/Day4/Homework/stranger.txt')
    text = f.read()
    f.close()
    text_list = text.split(" ")  #split function automatically returns a list. no need to make empty list beforehand
    return text_list


class Text:

    text_list = get_text_from_file()
    counts = Counter(text_list)

    def __init__(self, word):
        self.word = word
    
    def word_frequency(self, word): 
        self.word = word
        # text_list = get_text_from_file()
        # user_input = str(input("pick a word to view it's frequency\n"))
        # counts = Counter(text.text_list)
        if self.word in Text.counts:
            print(Text.counts[self.word])
        else:
            print("error")
            return

    def most_common(self):
        # text_list = get_text_from_file()
        highest_count = Text.counts.most_common(1)
        print(highest_count)

    def unique(self):
        unique_list = []
        for key, value in Text.counts.items():
            if 1 == value:
                return key
                
    
   
t1= Text("he")
# t1.word_frequency("he")
# t1.most_common()C
print(t1.unique())


