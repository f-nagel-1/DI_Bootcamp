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


//# 3

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona", 
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"], 
    "number_stores": 7000,
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US": ["pink", "green"],
    }
}


more_on_zara = {
    "creation_date" : 1975,
    "number_stores" : 10000,
}


brand["number_stores"] = 2

# print("Zaras clients are:", brand["type_of_clothes"][0], "," , brand["type_of_clothes"][1], "," , brand["type_of_clothes"][2])

#5
brand["country_creation"] = "Spain"

#6

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

#7
brand.pop("creation_date")

#8
print(brand["international_competitors"][-1])

#9
print(brand["major_color"]["US"])

# 10. 
print(len(brand))

# 11. 

for key, value in brand.items():
    print(value)

# . Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

brand.update(more_on_zara)
print(brand)