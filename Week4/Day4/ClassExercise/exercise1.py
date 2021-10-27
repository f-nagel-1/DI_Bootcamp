
# def say_hello(name, age, profession):
#     print(f"hello {name}, I am {age} years old and I work as {profession}!")

# say_hello("toby", 34, "coder")


# def calculation(a,b):
#     return a+b, a-b

# res = calculation(40,10)
# print()

def check_arguments(*args):
    print(f"These are the arguments {args}")
check_arguments(1, 2, 'hey')
>> These are the arguments (1, 2, 'hey') // You get a tuple