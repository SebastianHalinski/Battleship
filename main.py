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
            multiplayer_game()

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
        break


def get_correct_locations():
    list_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    list_num = [str(num) for num in range(1, 11)]
    correct_locations = []
    for a in list_alfa:
        for b in list_num:
            correct_locations.append(a + b)
    return correct_locations


def multiplayer_game():

    print("First player")
    first_player_name = input("Enter the name of the first player: ")
    first_player = Player(first_player_name)
    first_player.ocean.print_ocean(first_player.get_name())
    add_ships(first_player)
    input("Press any button to continue")
    #os.system("clear")
    print("Second player")
    second_player_name = input("Enter the name of second player: ")
    second_player = Player(second_player_name)
    second_player.ocean.print_ocean(second_player.get_name())
    add_ships(second_player)
    input("Press any button to continue")

    while True:
        print_waiting_screen("waiting_for_player_1.txt")
        first_player.ocean.print_ocean(first_player.get_name())
        second_player.ocean.print_ocean(first_player.get_name())
        while True:
            location = input("Enter your shoot location(like E6): ").upper()
            correct_locations = get_correct_locations()
            if location in correct_locations:
                x, y = convert_location_to_coordinates(location)
                break
        first_player.shoot(second_player, x, y)
        ship = first_player.get_ship_from_coordinates(second_player, x, y)
        if ship.is_sunk(second_player.get_ocean().get_board()):
            print("Ship is sunk")
        second_player.ocean.print_ocean(first_player.get_name())
        input("Press any button to continue")
        win = first_player.is_winner(second_player)
        if win == True:
            print_win_screen()
            main()

        first_player, second_player = second_player, first_player


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

    while True:
        location = input("Enter a ship location(like E6): ").upper()
        correct_locations = get_correct_locations()
        if location in correct_locations:
            x, y = convert_location_to_coordinates(location)
            break

    return x, y, is_horizontal



if __name__ == "__main__":
    main()
