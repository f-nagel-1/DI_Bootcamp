
import random

class Game:
    def __init__(self):
        pass

    def get_user_item(self):
        user_item = input("Please select an item (r)ock, (p)aper or (s)cissors   ")
        while (user_item != "r" and user_item != "p" and user_item != "s"):
            user_item = input("Wrong selection! Please select an item (r)ock, (p)aper or (s)cissors   ")
        return user_item

    def get_computer_item(self):
        computer_item = random.choice(["r", "p", "s"])
        return computer_item

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif user_item == "p" and computer_item == "s":
            return "loss"
        elif user_item == "p" and computer_item == "r":
            return "win"
        elif user_item == "r" and computer_item == "p":
            return "loss"
        elif user_item == "r" and computer_item == "s":
            return "win"
        elif user_item == "s" and computer_item == "p":
            return "win"
        elif user_item == "s" and computer_item == "r":
            return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        choice_dict = {
            "r" : "rock",
            "p" : "paper",
            "s" : "scissors"
        }
        result = self.get_game_result(user_item, computer_item)
        print("you selected: ", choice_dict[user_item], " the computer selected: ", choice_dict[computer_item], "you", result)
        return result


# g1 = Game()
# g1.play()