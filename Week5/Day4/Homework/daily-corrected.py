class Text:

    def __init__(self,string):
        self.content = string
    
    def word_frequency(self, word):
        word_list = self.content.split()
        if word in word_list:
            return f'the word {word} shows up {self.__word_frequency(word)} times'

    def __word_frequency(self,word):
        if word in self.word_list:
            return self.word_list.count(word)


    def most_commong_word(self):
        word_set = set(self.word_list)
        word = {}
        for word in word_set:
            word_dict.update({word:self.word_frequency((word))})

my_text = Text("hello world hello hello hello goodby world")
print(my_text.word_frequency("hello"))