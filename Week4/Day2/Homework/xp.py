# Exercise 1 : Favorite Numbers

# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.


my_fav_numbers = {3, 13, 18}
print(my_fav_numbers)

my_fav_numbers.add(15)
my_fav_numbers.add(22)
print(my_fav_numbers)

number_list = list(my_fav_numbers)
number_list.pop()

new_set = set(number_list)

friend_fav_numbers = {7, 15, 99}
our_fav_numbers = new_set | friend_set



# Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

No, existing tuples cannot be changed, however it is possible to slice them and create new tuples with the desired values.


# Exercise 3: Print A Range Of Numbers
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.


range_numbers = range(1, 21)

for element in range_numbers:
    print(element)



# Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
integers are "full" numbers, whereas floats are numbers with decimal points
# Can you think of another way to generate a sequence of floats?
dividing uneven numbers with 2

# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).


my_numbers = []

for number in range(2,6):
    my_numbers.append(number)
    new_number = float(number) - 0.5
    my_numbers.append((new_number))

my_numbers.sort() 
print(my_numbers)



# Exercise 5: Shopping List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"];

basket.remove("Banana")
basket.pop()
basket.append("Kiwi")
basket.insert(0, "Apples")
basket.count("Apples")
basket.clear()
print(basket)


# Exercise 6 : Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.


my_name = "elena"

while True:
    user_name = input("please state your name\n")
    if user_name.lower() == my_name:
        print("Great name")
        break
    else: 
        print("Try a better name")


# Exercise 7
# Given a list, use a loop to print out every element which has an even index.

basket = ["Banana", "Apples", "Oranges", "Blueberries", "Kiwis", "bread", "potatoes", "chips", "garlic"];

for number in range(0,10,2):
    print(basket[number])




# Exercise 8
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for number in range (1500, 2501):
    if number%5 == 0 and number%7 == 0:
        print(number)


# Exercise 9: Favorite Fruits
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.


user_favs = input("what are your favorite fruits? Please enter them with a space in between\n").split(" ")

while True:
    user_list = list(user_favs)
    any_fruit = input("list a fruit\n")
    if any_fruit in user_list:
        print("You chose one of your favorite fruits! Enjoy!")
        break
    else: 
        print("You chose a new fruit. I hope you enjoy")


# Exercise 10: Who Ordered A Pizza ?

# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

active = True

list_toppings = []
while active:
    topping = input("Please state your pizza topping\n")
    if topping == "quit":
        active = False
        topping_costs = len(list_toppings) * 2.5
        print(10 + topping_costs)

    else:
        list_toppings.append(topping)
        print("great. what else?")
        


# Exercise 11: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.



total_sum = 0
price_baby = 0
price_child = 10
price_adult = 15


number_people = int(input("how many in your family want to see a movie?\n"))

for person in range (0,number_people):
    age = int(input("what is your age?\n"))
    if age < 3:
        total_sum += price_baby
    elif age > 3 and age< 12:
        total_sum += price_child
    elif age > 12:
        total_sum += price_adult

print("the cost of your tickets is: ", total_sum)


# //Exercise 12 : Who Is Under 16?
# Given a list of names, write a program that asks every user for their age, if they are less than 16 years old remove them from the list.
# At the end, print the final list.

names_list = ["david", "anna", "sarah"]
age = ""
names_adults = []

for name in names_list:
    age = int(input(" what is your age?\n"))
    if age > 16:
        names_adults.append(name)

print("These are over 16", names_adults)




# //Exercise 13
# Instructions
# Make a list called sandwich_orders and fill it with the names of various sandwiches .
# Then make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.


sandwich_orders = ["reuben", "cucumber", "club"]

finished_sandwiches = []

for element in sandwich_orders:
    finished_sandwiches.append(element)


for item in finished_sandwiches:
    print("I made your", item, "sandwich")





# pastrami_var = "pastrami"

# sandwich_orders.extend([pastrami_var for i in range(3)])
# print(sandwich_orders)

sandwich_orders = ["reuben", "pastrami", "cucumber", "pastrami", "club", "pastrami"]

finished_sandwiches = []

print("sorry, all out of pastrami")


for element in sandwich_orders:
    sandwich_orders.remove("pastrami")
    finished_sandwiches.append(element)


for item in finished_sandwiches:
    print("I made your", item, "sandwich")


