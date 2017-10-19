import os
import sys
import random

from ocean import Ocean
from player import ComputerPlayer, Player
from ship import Ship
from square import Square


def menu():
    print( """Select option:

Press 1 to start multiplayer game
Press 2 to start singleplayer game
Press 3 to learn how to play
Press 4 to see the Hall of Fame
Press 0 to exit

""")


def press_enter_to_continue():
    input('Press enter to continue: ')


def read_screen(file_name):
    with open(file_name) as file:
        contents = file.read()
    return contents


def print_screen(file_name):
    os.system('clear')
    screen = read_screen(file_name)
    print(screen)
    input('Press enter to continue: ')
    os.system('clear')


def get_correct_locations():
    list_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    list_num = [str(num) for num in range(1, 11)]
    correct_locations = []
    for a in list_alfa:
        for b in list_num:
            correct_locations.append(a + b)
    return correct_locations


def convert_location_to_coordinates(location):
    y = int(location[1:]) - 1

    x_cords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in x_cords:
        if location[0] == i:
            x = int(x_cords.index(i))

    return x, y


def get_is_horizontal():
    possible_answers = ('H', 'h', 'V', 'v')
    answer_to_is_horzontal = {'H': True, 'V': False}
    answer = None
    while answer not in possible_answers:
        answer = input("Enter H to place ship horizontally or V to place ship vertically: ").upper()
    is_horizontal = answer_to_is_horzontal[answer]

    return is_horizontal


def get_location():
    correct_locations = get_correct_locations()
    location = None
    while location not in correct_locations:
        location = input("Enter the ship's location (e. g. E6): ").upper()

    return location


def human_add_ships(player):
    ocean = player.get_ocean()
    print("Place your ships on board!")
    for ship_type in Ship.SHIP_TYPE_TO_LENGTH:
        ship_length = Ship.SHIP_TYPE_TO_LENGTH[ship_type]
        print("{} is {} squares long".format(ship_type, ship_length))

        is_horizontal = get_is_horizontal()
        location = get_location()
        x, y = convert_location_to_coordinates(location)
        result = ocean.add_ship(x, y, is_horizontal, ship_type)
        while not result:
            print("Wrong location! Try again")
            is_horizontal = get_is_horizontal()
            location = get_location()
            x, y = convert_location_to_coordinates(location)
            result = ocean.add_ship(x, y, is_horizontal, ship_type)

        ocean.print_ocean(player.get_name())
        break


def choose_random_location():
    x = random.randrange(Ocean.width)
    y = random.randrange(Ocean.height)

    return x, y


def computer_add_ships(computer):
    ocean = computer.get_ocean()
    x, y = computer.choose_random_location()
    for ship_type in Ship.SHIP_TYPE_TO_LENGTH:
        ship_length = Ship.SHIP_TYPE_TO_LENGTH[ship_type]
        x, y = computer.choose_random_location()
        is_horizontal = random.choice([True, False])

        result = ocean.add_ship(x, y, is_horizontal, ship_type)
        while not result:
            x, y = choose_random_location()
            is_horizontal = random.choice([True, False])
            result = ocean.add_ship(x, y, is_horizontal, ship_type)


def set_up_player():
    player_name = None
    while not player_name:
        player_name = input("What's your name? ")
    player = Player(player_name)
    ocean = player.get_ocean()
    ocean.print_ocean(player_name)
    human_add_ships(player)
    press_enter_to_continue()
    os.system("clear")

    return player


def multiplayer_game():
    waiting_screen = "waiting_for_player_1.txt"
    waiting_screen_2 = "waiting_for_player_2.txt"

    print_screen("waiting_for_player_1.txt")
    player_1 = set_up_player()
    print_screen("waiting_for_player_2.txt")
    player_2 = set_up_player()
    player, enemy = player_1, player_2

    while True:
        player_ocean = player.get_ocean()
        enemy_ocean = enemy.get_ocean()
        player_name = player.get_name()
        enemy_name = enemy.get_name()

        print_screen(waiting_screen)
        player_ocean.print_ocean(player_name)
        enemy_ocean.print_ocean(player_name)

        shot_location = get_location()
        x, y = convert_location_to_coordinates(shot_location)
        result = player.shoot(enemy, x, y)
        while not result:
            print('You tried to hit this place before. Try again!')
            shot_location = get_location()
            x, y = convert_location_to_coordinates(shot_location)
            result = player.shoot(enemy, x, y)

        possible_ship = player.get_ship_from_coordinates(enemy, x, y)
        if possible_ship:
            ship = possible_ship
            if ship.is_sunk(enemy_ocean.get_board()):
                print("{} is sunk!".format(ship.ship_type))

        enemy_ocean.print_ocean(player_name)
        press_enter_to_continue()

        if player.is_winner(enemy):
            print_screen('you_win.txt')
            main()

        player, enemy = enemy, player
        waiting_screen = waiting_screen_2


def main():
    print_screen('intro.txt')

    while True:
        menu()
        user_input = input("Your choice: ")

        if user_input == "1":
            multiplayer_game()

        elif user_input == "2":
            single_game()

        elif user_input == "3":
            print_screen('how_to_play.txt')

        elif user_input == '4':
            print_hall_of_fame()

        elif user_input == "0":
            break

        else:
            print('\nWrong input!\n')


# if __name__ == "__main__":
#     main()


player = Player('Asia')
computer = ComputerPlayer('easy')
computer_add_ships(computer)
computer.get_ocean().print_ocean('Computer')

shot = computer.choose_shot()
computer.shoot(player, *shot)