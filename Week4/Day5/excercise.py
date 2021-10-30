# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Suppose the following input is supplied to the program:
# without,hello,bag,world

# Then, the output should be:
# bag,hello,without,world

# sentence = str(input("Please enter a few words seperated by comma\n"))

# list_words = sentence.split(",")
# list_words.sort()
# print(list_words)

# print([x for x in sorted((str(input("Please enter a few words seperated by comma\n"))).split(","))])


print(','.join([x for x in sorted(str(input("Please enter a few words seperated by comma\n")).split(","))]))



# print = (','.join([str(x) for x in sorted((str(input("Please enter a few words seperated by comma\n"))).split(","))]))


# ','.join

# print( ','.join([str(x)x in sorted((str(input("Please enter a few words seperated by comma\n"))).split(","))])  )

# newlist = [x.upper() for x in fruits]