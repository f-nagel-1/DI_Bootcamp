from game import Game

# get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation), and return the choice. No looping should occur here.
# The possibles choices are : Play a new game or Show scores or Quit

def get_user_menu_choice():
    # res = isinstance(test_string, str)
    user_selection = input("Menu\n (g) Play a new game\n (x) Show scores and exit\n")
    if isinstance(user_selection, str):
        user_selection = user_selection.lower()
        if user_selection == "g":
            print("you want to start the game")
            return user_selection
        elif user_selection == "x":
            print("Here are the results")
            return user_selection
        else:
            return "w"
    else:
        return "w"
    

# print_results(results) – this should print the results of the games played. 
# It should have a single parameter named results; which will be a dictionary of the results of the games played. It should display these results in a user-friendly way, and thank the user for playing.
        
def print_results(results):
    print("    Game Results:\nYou won:", results["win"], "times\nYou loss:", results["loss"], "times\nYou draw:", results["draw"], "times\n ")


# Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)

def main():
    results_dict = {
        "win" : 0,
        "loss" : 0,
        "draw" : 0
    }
    user_choice = get_user_menu_choice()
    while user_choice == "g" or user_choice == "w":
        if user_choice == "g":
            newGame = Game()
            result = newGame.play()
            results_dict[result] = results_dict[result] + 1
            user_choice = get_user_menu_choice()
        else:
            user_choice = get_user_menu_choice()
    else:
        print_results(results_dict)
    

main()
