import psycopg2
import psycopg2.extras


HOSTNAME = 'localhost'
PORTID = 5432
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'menu'

def connect(query, fetch):
    try:
        connection = psycopg2.connect(host=HOSTNAME, port=PORTID, user=USERNAME, password=PASSWORD, dbname=DATABASE )
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(query)
        if fetch is True:
            results = cursor.fetchall()
        else:
            results = 'successful'
        connection.commit()
        connection.close()
        return results
    except Exception as error:
        print(error)


class MenuItem():
    #def __init__(self, name, price):
        #self.name = name
        #self.price = price

    def save(name, price):
        fetch = False
        query = f"insert into menu (name, price) values ('{name}', {price});"
        connect(query, fetch)
        message = "Item was created successfully"
        return message

    def delete(name):
        fetch = False
        query = f"delete from menu where name = ('{name}');"
        connect(query, fetch)
        message = "Item was deleted successfully"
        return message

    def update(name, price):
        fetch = False
        query = f"update menu set price = {price} where name = '{name}'; "
        connect(query, fetch)
        message = "Item was updated successfully"
        return message

    def all():
        fetch = True
        query = f"select * from menu"
        results = connect(query, fetch)
        dict_results = {}
        for record in results:
            #print('item name = {}\nitem price = {}'.format(record['name'],record['price']))
            dict_results[record['name']] =record['price']
        return dict_results

        


# Create another method called get_by_name that will return a single MenuItem object depending on it’s name, if an object is not found (there is no item matching the name in the get_by_name method) return None.

    def get_by_name(name):
        fetch = True
        query = f"select * from menu where name = '{name}'; "
        results = connect(query, fetch)
        for record in results:
            print('item name = {}\nitem price = {}'.format(record['name'],record['price']))

def main():
    #item = MenuItem('Second Burger', 25)
    #item.save()
    # print("After adding Imperial Burger:\n", MenuItem.all())
    #item2 = MenuItem.update('Imperial Burger', 10)
    #item = MenuItem.all()
    item3 = MenuItem.get_by_name('Imperial Burger')
#main()