#ex1

def display_message():
    print("Hey, I am confused")

display_message()


# ex2

def favorite_book(title):
    print(f'One of my favorite books is {name}')

favorite_book("Alice in Wonderland")

#ex3

def describe_city(city, country='Iceland'):
    print(f'{city} is in {country}')
describe_city('Reykjavik ')

#Ex4 : 
def random_number(number):
    number2 = random.randint(0, 100)
    if number2==number:
        print('Congrats!')
    else:
        print('You failed')
        print(f'Your number was {number} and the computer number was {number2}')
random_number(10)


# Exercise 6 : 
magician = ["david","bob","erin"]

def show_magicians(magician):
    for name in magician:
        print(name)
show_magicians(magician)

great_magicians = []

def make_great(magician):
    while magician:
        name = magician.pop()
        great_magician = name + ' the Great'
        great_magicians.append(great_magician)
    
    for great_magician in great_magicians:
        magician.append(great_magician)
    

make_great(magician)
show_magicians(magician)