from ocean import Ocean
from player import ComputerPlayer, Player
from ship import Ship
from square import Square
from printing import *
import sys
import os


def menu():
    print( """Select option:

Press 1 to start multiplayer game
Press 2 to start singleplayer game
Press 3 to learn how to play
Press 4 to see the Hall of Fame
Press 0 to exit

""")


def main():
    print_starting_screen()
    user_input = ""

    while True: #user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" and user_input != "0":

        os.system('clear')
        menu()

        user_input = input("Your choice: ")
        if user_input == "1":
            first_player_name = input("Enter the name of the first player: ")
            second_player_name = input("Enter the name of second player: ")
            first_player = Player(first_player_name)
            second_player = Player(second_player_name)
            multiplayer_game(first_player, second_player)

        elif user_input == "2":
            player_name = input("Enter your name: ")
            player = Player(player_name)
            single_name(player_name)

        elif user_input == "3":
            print_how_to_play()

        elif user_input == '4':
            print_hall_of_fame()

        elif user_input == "0":
            exit()


def add_ships(player):
    ocean = player.get_ocean()
    print("Place your ships on board!")
    for ship_type in Ship.SHIP_TYPE_TO_LENGTH:
        ship_length = Ship.SHIP_TYPE_TO_LENGTH[ship_type]
        print("{} is {} squares long".format(ship_type, ship_length))
        x, y, is_horizontal = get_ship_details()
        result = ocean.add_ship(x, y, is_horizontal, ship_type)
        while not result:
            print("Wrong location! Try again")
            x, y, is_horizontal = get_ship_details()
            result = ocean.add_ship(x, y, is_horizontal, ship_type)
        ocean.print_ocean(player.get_name())


def multiplayer_game(first_player, second_player):

    add_ships(first_player)
    os.system("clear")
    print("Second player")
    add_ships(second_player)

    while True:
        print_waiting_screen("waiting_for_player_1.txt")
        first_player.ocean.print_ocean(first_player.get_name())
        second_player.ocean.print_ocean(first_player.get_name())
<<<<<<< Updated upstream
        while True:
            location = input("Enter a your shoot location(like E6): ").upper()
            list_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            if location[0] in list_alfa and location[1:].isnumeric() and int(location[1:]) <= 10:
                x, y = conver_location_to_coordinates(location)
                break
=======
        location = input("Enter a your shoot location(like E6): ")
        x, y = convert_location_to_coordinates(location)
>>>>>>> Stashed changes
        first_player.shoot(second_player, x, y)
        second_player.ocean.print_ocean(first_player.get_name())
        input()
        win = first_player.is_winner(second_player)
        if win == True:
            exit()
    #Funkcja pokazujca plansze swoja i przeciwnika

    #Funkcja strzal


def convert_location_to_coordinates(location):
    y = int(location[1:]) - 1

    x_cords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in x_cords:
        if location[0] == i:
            x = int(x_cords.index(i))

    return x, y


def get_ship_details():

    is_horizontal = input("Enter H to place ship horizontally or V to place ship vertically: ")
    while is_horizontal != "H" and is_horizontal != "h" and is_horizontal != "V" and is_horizontal != "v":
        is_horizontal = input("Enter H to place ship horizontally or V to place ship vertically: ")

    if is_horizontal == "H" or is_horizontal == "h":
        is_horizontal = True
    else:
        is_horizontal = False

<<<<<<< Updated upstream
    while True:
        location = input("Enter a ship location(like E6): ").upper()
        list_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        if location[0] in list_alfa and location[1:].isnumeric() and int(location[1:]) <= 10:
            x, y = conver_location_to_coordinates(location)
            break
=======
    location = input("Enter a ship location(like E6): ").upper()
    x, y = convert_location_to_coordinates(location)
>>>>>>> Stashed changes

    return x, y, is_horizontal


if __name__ == "__main__":
    main()
