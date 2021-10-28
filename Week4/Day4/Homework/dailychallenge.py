import re

matrix = [

    ["7", "i","3"],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", " ", "#"],
    ["s", "M", " "],
    ["$", "a", " "],
    ["#", "t", "%"],
    ["^", "r", "!"],

]
#len(matrix(0)) refers to length of the first entry so length on 7i3, so for each element of 7i3
#, then specify the range of the entire matrix whcih would be 8 lines (the column)
for row in range(len(matrix[0])):
    for column in range(len(matrix)):
         print(matrix[row][column])

# lower_accept_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

# upper_accept_letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


# vertical1 = [i[0] for i in matrix]
# vertical2 = [i[1] for i in matrix]
# vertical3 = [i[2] for i in matrix]

# res = str(''.join([str(item) for item in vertical1]))+(''.join([str(item) for item in vertical2]))+(''.join([str(item) for item in vertical3]))

# sentence = ""


# for letter in res:
    
#     if letter in lower_accept_letter or letter in upper_accept_letter:
#         sentence += letter
#     elif letter==' ' or letter=='#':
#         sentence +=" "


# print(sentence)

