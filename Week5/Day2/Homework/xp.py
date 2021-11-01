class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

# # Create another cat bread. In order to do so, create a class which inherits from the Cat class.#


class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# # Create a few cat instances.

anotherCat = Cat("Lou", 10)
print(anotherCat.walk())

secondCat = Bengal("Anna", 5)
print(secondCat.sing("meow meow meow"))


# # Create a list called my_cats, which will hold all the created cat instances.

my_cats = [anotherCat, secondCat]

# # Create a variable called my_pets. Its value is an instance of the Pet class.
# # Hint : Use the my_cats variable to create the instance.

my_pets = Pets(my_cats)

# # Take all the cats for a walk, use the walk method.

my_pets.walk()


# ###Create a class called Dog with the following attributes name, age, weight.
# Create 3 dogs and run them through your class.

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

# bark: returns a string which states: “<dog_name> is barking”.

    def bark(self):
        return f'{self.name} is barking'

# run_speed: returns the dogs running speed (weight/age*10).

    def run_speed(self):
        return (self.weight/self.age)*10

# fight : takes a parameter which value should be another dog called other_dog, returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
    def fight(self, other_dog):
        if (self.run_speed()*self.weight) > (other_dog.run_speed()*other_dog.weight):
            return f'{self.name} won the fight'
        else:
            return f'{other_dog.name} won the fight'


# Create 3 dogs and run them through your class.

rex = Dog("Rex", 2, 20)
polly = Dog("Polly", 4, 50)
woofy = Dog("Woofy", 5, 10)
print(woofy.bark())
print(rex.bark())
print(rex.run_speed())
print(rex.fight(polly))