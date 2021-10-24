

name = input('what is your name?')
age = input('what is your age?')
if age.isnumeric():
    age = int(age)

else:
    print("word")
    exit() #exit stops the program

print((name + " ") * age)

#print((name + " ") * age)

# intro_sen = f"hello my name is {name}"
#intro_sen = "hello my name is {}, I am {} years old". format(name,age) #format is
#print(intro_sen)

#if age > 30: #with if output has to be bolean. COLON IMPORTANT
#    print("you are that young")
#else:
  #  print("sausage")


#print("we are done") # part of global scope and therefore not part of the if statement


#intro_sen = "hello my name is {}, \nI am {} years old". format(name,age) #new line with \n
#print(intro_sen)

#if age > 60 and name == "tobyy":  #either condition true
  #  print("you are that young")
#elif age > 30 and name == "toby": #does not print because first condition name === toby is true, ergo order important
   # print("you are not toby")
#else:
    #print("sausage")