date = input("When were you born, please enter the date in the following format DD/MM/YYYY\n")

day, month, year = date.split("/")

user_year = int(year)
current_year = 2021
age = current_year - user_year

last_digit = age%10
number_is= "i" * last_digit

top = "__"
side = "|"

happy_str = "happy"
n = 1 
chunks = [happy_str[i:i+n] for i in range(0, len(happy_str), n)]
new_line = " : ".join(chunks)


underline = "_" * (len(new_line))
roof = "^" * (len(new_line)+8) 


print("     ", top * 3 , number_is, top * 3, "   ")
print("    ", side, new_line, side, "   ")
print(" ", top, side, underline, side, top, " ")
print (side, roof, side)