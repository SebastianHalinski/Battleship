import csv
import os
import random

import texttable as tt
from high_scores import *
from ocean import Ocean
from player import ComputerPlayer, Player
from ship import Ship
from square import Square


def high_score(level, shots):
    total_shots = shots
    all_ships_lenght = 17
    if level == 'EASY':
        level_multiplier = 100
    elif level == 'MEDIUM':
        level_multiplier = 200
    elif level == 'HARD':
        level_multiplier = 400
    score = int(level_multiplier * all_ships_lenght / total_shots)
    return score


def add_shot(shots):
    shots += 1
    return shots


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


def choose_random_location():
    x = random.randrange(Ocean.width)
    y = random.randrange(Ocean.height)

    return x, y


def computer_add_ships(computer):
    ocean = computer.get_ocean()
    for ship_type in Ship.SHIP_TYPE_TO_LENGTH:
        ship_length = Ship.SHIP_TYPE_TO_LENGTH[ship_type]
        x, y = choose_random_location()
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


def human_turn(player, enemy):

    player_ocean = player.get_ocean()
    enemy_ocean = enemy.get_ocean()
    player_name = player.get_name()
    enemy_name = enemy.get_name()

    print("{}, your turn!".format(player_name))
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

    return player.is_winner(enemy)


def computer_turn(computer_player, enemy):
    enemy_ocean = enemy.get_ocean()
    x, y = computer_player.choose_shot()
    computer_player.shoot(enemy, x, y)
    possible_ship = computer_player.get_ship_from_coordinates(enemy, x, y)
    if possible_ship:
        ship = possible_ship
        if ship.is_sunk(enemy_ocean.get_board()):
            print("{} is sunk!".format(ship.ship_type))


def single_game(difficulty_level):
    shots = 0
    human_player = set_up_player()
    computer_player = ComputerPlayer(difficulty_level)
    computer_ocean = computer_player.get_ocean()
    computer_add_ships(computer_player)

    while True:
        human_turn(human_player, computer_player)
        shots = add_shot(shots)
        if human_player.is_winner(computer_player):
            score = high_score(difficulty_level, shots)
            player_data = player_score(score, shots, difficulty_level, human_player.get_name())
            high_scores_data = import_hall_of_fame('high_scores.csv', player_data)
            print(get_highscore_table(high_scores_data, player_data, 'high_scores.csv'))
            export_hall_of_fame('high_scores.csv', high_scores_data)
            press_enter_to_continue()
            print_screen('you_win.txt')
            break
        computer_turn(computer_player, human_player)
        if computer_player.is_winner(human_player):
            print_screen('you_lose.txt')
            break


def multiplayer_game():
    waiting_screen = "waiting_for_player_1.txt"
    waiting_screen_2 = "waiting_for_player_2.txt"

    print_screen("waiting_for_player_1.txt")
    player_1 = set_up_player()
    print_screen("waiting_for_player_2.txt")
    player_2 = set_up_player()
    player, enemy = player_1, player_2

    while True:
        print_screen(waiting_screen)
        is_winner = human_turn(player, enemy)
        if is_winner:
            print_screen('you_win.txt')
            break
        player, enemy = enemy, player
        waiting_screen, waiting_screen_2 = waiting_screen_2, waiting_screen


def main():

    menu = """Select option:

    Press 1 to start multiplayer game
    Press 2 to start singleplayer game
    Press 0 to exit

    """

    difficulty_menu = """Choose difficulty level:
    ==> EASY
    ==> MEDIUM
    ==> HARD
    """

    print_screen('intro.txt')

    while True:
        print(menu)
        user_input = input("Your choice: ")

        if user_input == "1":
            multiplayer_game()

        elif user_input == "2":
            difficulty_level = input(difficulty_menu).upper()
            correct_levels = ("EASY", "MEDIUM", "HARD")
            while difficulty_level not in correct_levels:
                difficulty_level = input(difficulty_menu).upper()
            single_game(difficulty_level)

        elif user_input == "0":
            break

        else:
            print('\nWrong input!\n')


if __name__ == "__main__":
    main()
