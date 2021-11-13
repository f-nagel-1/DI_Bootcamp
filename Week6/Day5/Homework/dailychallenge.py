import psycopg2
import psycopg2.extras
import random
import requests
import json


HOSTNAME = 'localhost'
PORTID = 5432
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'country'


def get_country(n):
    url = 'https://restcountries.com/v3.1/all'
    data = requests.get(url)
    data = data.json()
    sample_data = random.sample(data, n)
    connection = psycopg2.connect(host=HOSTNAME, port=PORTID, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute()
    connection.commit()
    connection.close()


get_country()