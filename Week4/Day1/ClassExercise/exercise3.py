# Ask the user for a number betwee 1 and 100

# If the number is a multiple of three, print "Fizz"

# If the number is a multiple of five, print "Buzz".

# If the number is a multiple is a multiples of both three and five, print "FizzBuzz" instead.

number = int(input("pick a number\n"))


if number % 5 == 0 and number % 3 == 0:
    print("fizzbuzz")

elif number % 3 == 0:
    print("fuzz")

elif number % 5 == 0:
    print("buzz")

