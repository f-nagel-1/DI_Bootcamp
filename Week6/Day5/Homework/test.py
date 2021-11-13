import psycopg2

HOSTNAME = 'localhost'
PORTID = 5432
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'new_menu'

try:
    connection = psycopg2.connect(host=HOSTNAME, port=PORTID, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    cursor = connection.cursor()
    insert = "INSERT INTO menu_item VALUES ('Burger2', 15);"
    #insert_values = ('Burger2', 35)
    cursor.execute(insert)
    # results = cursor.fetchall()
    results = 'successful'
    connection.commit()
    connection.close()
    # return results
except Exception as error:
    print(error)



