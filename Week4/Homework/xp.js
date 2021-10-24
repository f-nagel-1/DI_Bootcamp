// exercise 1
print("hello world \n" *4)

//exercise 2

(99**3)*8

//exercise 3

5 < 3  //false
3 == 3 //true
3 == "3" //false
"3" > 3  //not defined
"Hello" == "hello" // false


//exercise 4


computer_brand = "lenovo"
print("I have a {} computer".format(computer_brand))


//exercise 5


my_name = "elena"
age = 33
shoe_size = 38
info = "my name is {} and my age is {} and my interesting shoe size is {}".format(my_name, age, shoe_size)
print(info)


//exercise 6



a = 15
b = 3

if a > b:
    print("hello world")



// //exercise 7
// Write code that asks the user for a number and determines whether this number is odd or even.

user_number = int(input("what is your number?\n"))
if user_number % 2 == 0:
    print("this is even")
else:
    print("this is uneven")



//exercise 8

// Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

user_name = input("what is your name?\n").lower()
if user_name == "elena":
    print("yo dude, cool name!")
else:
    print("sorry that you suck")


//exercise 9



user_height = int(input("what is your height?\n"))

if user_height > 145:
    print("you are tall enough")
else:
    print("you gotta grow more!")