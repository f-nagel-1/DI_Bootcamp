# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other dogs (use *args). The method should print the following string: “dog_names all play together”.

from xp import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(self, trained=False)

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self):
        #no idea what goes on here


# nothing works. no idea why
doggy = Dog("Doggy", 3, 12)
petDoggy = PetDog(doggy)
print(petDoggy.train())