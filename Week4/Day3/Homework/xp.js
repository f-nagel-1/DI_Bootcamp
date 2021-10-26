// Exercise 1 : Convert Lists Into Dictionaries

// Convert the two following lists, into dictionaries.
// Hint: Use the zip method
// keys = ['Ten', 'Twenty', 'Thirty']
// values = [10, 20, 30]
// Expected output:
// {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = dict(zip(keys, values))
print(dictionary)


// Exercise 2 : Cinemax #2

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


total_sum = 0
price_baby = 0
price_child = 10
price_adult = 15


for person, age in family.items():
    if age < 3:
        total_sum += price_baby
        print(f'{person}, your fee is: ', price_baby)
    elif age > 3 and age< 12:
        total_sum += price_child
        print(f'{person}, your fee is: ', price_child)
    elif age > 12:
        total_sum += price_adult
        print(f'{person}, your fee is: ', price_adult)


print("the cost of your tickets is: ", total_sum) 


//