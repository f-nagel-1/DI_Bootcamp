import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",

         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

y = json.loads(sampleJson)


print(y["company"]["employee"]["payable"]["salary"])
y["company"]["employee"]["birth_date"] = "13/05/1980"
print(y["company"]["employee"])

# Save the dictionary as JSON to a file.
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.

with open('C:/Users/Fenriz/Desktop/DI/HTML/DI_Bootcamp/Week5/Day4/Homework/data.json', 'w+') as fp:
    json.dump(y, fp)
