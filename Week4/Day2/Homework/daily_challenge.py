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
new_line = ":".join(chunks)


underline = "_" * (len(new_line))
roof = "^" * (len(new_line)+10) 

birthday_str = "Birthday"
n = 1 
parts = [birthday_str[i:i+n] for i in range(0, len(birthday_str), n)]
birthday_line = ":".join(parts)
full_length = len(birthday_line)


underline = "_" * (full_length + 2)
roof = "^" * full_length
line_short = len(underline) - 8
underline_short = "_" * line_short
spaces = " " * full_length
bottom = "~" * (full_length + 4)

print("   ", top, number_is, top)
print("  ", side, new_line, side, "  ")
print(top, side, underline_short, side, top)
print(side, roof, side)
print(side, birthday_line,side)
print(side, spaces, side)
print(bottom)