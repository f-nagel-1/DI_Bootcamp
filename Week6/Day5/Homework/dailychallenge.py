import psycopg2
import psycopg2.extras
import random
import requests

HOSTNAME = 'localhost'
PORTID = 5432
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'country'


def get_country():
    # connection = psycopg2.connect(host=HOSTNAME, port=PORTID, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    # cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # cursor.execute(query)
    # connection.commit()
    # connection.close()
#get the countries
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    data = response.json()
   
    #random_ten = random.sample(data, k=10)
    #print(random_ten)

    #for country in random_ten:
       #print(country['name']['common'], str(country['capital'][0]), country['flag'], country['subregion'], country['population'])

    #for country_data in random_ten:
        #print(country_data['name']['common'])

    for index_country in range(10):
        index_country = random.randint(0,len(data))
        #print(data[index_country]['name']['common'])
        print(data[index_country]['name']['common'], str(data[index_country]['capital'][0]), data[index_country]['flag'], data[index_country]['subregion'], data[index_country]['population'])

get_country()



 #number_country = random.randint(1,10)
 #for country in range(1,10):
    #print(country)


