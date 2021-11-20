import psycopg2
import psycopg2.extras
import requests

HOSTNAME = 'localhost'
PORTID = 5432
USERNAME = 'postgres'
PASSWORD = 'postgres'
DATABASE = 'bored'


def display_menu():
    #starting screen
    user_choice = input("To get a random activity please enter: r\n To get a customized activity by answering questions please enter: c\n To exit please enter: x\n")
    if user_choice == "r":
        show_random()
    if user_choice == "c":
        custom()

def custom():
    #customized suggestion based on user input
    activity = str(input("Choose the type of activity!\n For education, press (e).\n For recreational, press (r).\n For social, press (s).\n For diy press (d).\n For charity press (c).\n For relaxation press (re).\n For cooking press (co)\n For music press (m).\n For busywork press (b)\n"))
    #uses switcher function to turn user input into parameter from dictionary
    activity = type_activity(activity)
    #print(activity)
    participants = int(input("Please enter number of participants\n"))
    price = int(input("Please enter your budget\n"))

    #had to add the +activity parameter (from documentation) to make the get run faster. works as prefiltering
    url = 'https://www.boredapi.com/api/activity?type='+activity
    response = requests.get(url)
    data = response.json()
    
    #saves 
    query = f"INSERT INTO bored_ideas (activity, type_activity, participants, price, activity_key) VALUES ('{str(data['activity'])}', '{data['type']}','{participants}','{price}','{data['key']}') "
    print(data['activity'])  
        
    connection = psycopg2.connect(host=HOSTNAME, port=PORTID, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    connection.commit()
    connection.close()
    
    
def type_activity(activity):
    switcher = {
        "e" : "education",
        "r" : "recreational",
        "s" : "social",
        "d" : "diy",
        "c" : "charity",
        "re" : "relaxation",
        "m" : "music",
        "b" : "busywork",
        "co" : "cooking",

    }
    return switcher.get(activity)


def show_random():
    url = 'https://www.boredapi.com/api/activity'
    response = requests.get(url)
    data = response.json()
    query = f"INSERT INTO bored_ideas (activity, type_activity, participants, price, activity_key) VALUES ('{str(data['activity'])}', '{data['type']}','{data['participants']}','{int(data['price'])}','{data['key']}') "
    print(data['activity'])  
    
    connection = psycopg2.connect(host=HOSTNAME, port=PORTID, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    connection.commit()
    connection.close()
        

def main():
    print("Welcome to our idea-generator for when you are bored\n")
    while True:
        display_menu()
        c = input("Do you want to choose again? Press (n) for NO and (y) for YES\n")
        if c == "n":
            break
        

if __name__ == "__main__":
    main()

