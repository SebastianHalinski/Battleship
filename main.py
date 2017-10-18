from ocean import Ocean
from player import ComputerPlayer, Player
from ship import Ship
from square import Square
import os
menu = """Enter an action:

Press 1 to create game player versus player
Press 2 to create game player versus computer
Press 3 to quit
"""


def main():

    user_input = ""
    while user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4" and user_input != "0":
        print(menu)
        user_input = input("Enter: ")
        if user_input == "1":
            first_player_name = input("Enter a name of first player: ")
            second_player_name = input("Enter a name of second player: ")
            first_player = Player(first_player_name)
            second_player = Player(second_player_name)
            multiplayer_game(first_player, second_player)

        if user_input == "2":
            player_name = input("Enter a name of first player: ")
            player = Player(player_name)
            single_name(player_name)

        if user_input == "3":
            # how to play
            pass
        if user_input == '4':
            # Hall of fame
            pass
        if user_input == "0":
            exit()

def multiplayer_game(first_player, second_player):

    print("Place your ships on board!")
    print("First is Carrier(5 squares length)")
    x, y, is_horizontal = place_ship_on_ocean()
    ship = first_player.ocean.add_ship(x, y, is_horizontal, 'Carrier')
    while ship is not True:
        print("Wrong location! Try again")
        x, y, is_horizontal = place_ship_on_ocean()
        ship = first_player.ocean.add_ship(x, y, is_horizontal, 'Carrier')
    first_player.ocean.print_ocean(first_player)

    print("Second is Battleship(4 squares length)")
    x, y, is_horizontal = place_ship_on_ocean()
    ship = first_player.ocean.add_ship(x, y, is_horizontal, 'Battleship')
    while ship is not True:
        print("Wrong location! Try again")
        x, y, is_horizontal = place_ship_on_ocean()
        ship = first_player.ocean.add_ship(x, y, is_horizontal, 'Battleship')
    first_player.ocean.print_ocean(first_player)

    print("Third is Cruiser(3 squares length)")
    x, y, is_horizontal = place_ship_on_ocean()
    ship = first_player.ocean.add_ship(x, y, is_horizontal, 'Cruiser')
    while ship is not True:
        print("Wrong location! Try again")
        x, y, is_horizontal = place_ship_on_ocean()
        ship = first_player.ocean.add_ship(x, y, is_horizontal, 'Cruiser')
    first_player.ocean.print_ocean(first_player)

    print("Fourth is Submarine(3 squares length)")
    x, y, is_horizontal = place_ship_on_ocean()
    ship = first_player.ocean.add_ship(x, y, is_horizontal, 'Submarine')
    while ship is not True:
        print("Wrong location! Try again")
        x, y, is_horizontal = place_ship_on_ocean()
        ship = first_player.ocean.add_ship(x, y, is_horizontal, 'Submarine')
    first_player.ocean.print_ocean(first_player)

    print("Fifth is Destroyer(2 squares length)")
    x, y, is_horizontal = place_ship_on_ocean()
    ship = first_player.ocean.add_ship(x, y, is_horizontal, 'Destroyer')
    while ship is not True:
        print("Wrong location! Try again")
        x, y, is_horizontal = place_ship_on_ocean()
        ship = first_player.ocean.add_ship(x, y, is_horizontal, 'Destroyer')

    first_player.ocean.print_ocean(first_player)

    # funkcja ktora bedzie wolac drugiego player
    os.system("clear")
    print("Second player")

    print("Place your ships on board!")
    print("First is Carrier(5 squares length)")
    x, y, is_horizontal = place_ship_on_ocean()
    ship = second_player.ocean.add_ship(x, y, is_horizontal, 'Carrier')
    while ship is not True:
        print("Wrong location! Try again")
        x, y, is_horizontal = place_ship_on_ocean()
        ship = second_player.ocean.add_ship(x, y, is_horizontal, 'Carrier')
    second_player.ocean.print_ocean(second_player)

    print("Second is Battleship(4 squares length)")
    x, y, is_horizontal = place_ship_on_ocean()
    ship = second_player.ocean.add_ship(x, y, is_horizontal, 'Battleship')
    while ship is not True:
        print("Wrong location! Try again")
        x, y, is_horizontal = place_ship_on_ocean()
        ship = second_player.ocean.add_ship(x, y, is_horizontal, 'Battleship')
    second_player.ocean.print_ocean(second_player)

    print("Third is Cruiser(3 squares length)")
    x, y, is_horizontal = place_ship_on_ocean()
    ship = second_player.ocean.add_ship(x, y, is_horizontal, 'Cruiser')
    while ship is not True:
        print("Wrong location! Try again")
        x, y, is_horizontal = place_ship_on_ocean()
        ship = second_player.ocean.add_ship(x, y, is_horizontal, 'Cruiser')
    second_player.ocean.print_ocean(second_player)

    print("Fourth is Submarine(3 squares length)")
    x, y, is_horizontal = place_ship_on_ocean()
    ship = second_player.ocean.add_ship(x, y, is_horizontal, 'Submarine')
    while ship is not True:
        print("Wrong location! Try again")
        x, y, is_horizontal = place_ship_on_ocean()
        ship = second_player.ocean.add_ship(x, y, is_horizontal, 'Submarine')
    second_player.ocean.print_ocean(second_player)

    print("Fifth is Destroyer(2 squares length)")
    x, y, is_horizontal = place_ship_on_ocean()
    ship = second_player.ocean.add_ship(x, y, is_horizontal, 'Destroyer')
    while ship is not True:
        print("Wrong location! Try again")
        x, y, is_horizontal = place_ship_on_ocean()
        ship = second_player.ocean.add_ship(x, y, is_horizontal, 'Destroyer')

    second_player.ocean.print_ocean(second_player)

    # Funkcja ktora bedzie wolac 1 playera

    # gra start

    #Funkcja pokazujca plansze swoja i przeciwnika

    #Funkcja strzal



def place_ship_on_ocean():

    is_horizontal = input("Enter H to place ship horizontal or V to place ship vertical")
    while is_horizontal != "H" and is_horizontal != "h" and is_horizontal != "V" and is_horizontal != "v":
        is_horizontal = input("Enter H to place ship horizontal or V to place ship vertical")

    if is_horizontal == "H" or is_horizontal == "h":
        is_horizontal = True
    else:
        is_horizontal = False

    location = input("Enter a ship location(like E6): ").upper()
    x, y = conver_location_to_coordinates(location)

    return x, y, is_horizontal


def conver_location_to_coordinates(location):
    y = int(location[1]) - 1

    x_cords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in x_cords:
        if location[0] == i:
            x = int(x_cords.index(i))

    return x, y


if __name__ == "__main__":
    main()





# s = Square(1, 1, Square.SQUARE_STATES['empty'])
# print(s)
# s.change_status_to_hit()
# print(s)
# s.change_status_to_missed()
# print(s)
# print(s.get_status())
# print(s.get_status_empty())
# print(s.get_status_ship())
# print(s.get_status_hit())
# print(s.get_x())
# print(s.get_y())

# s1 = Ship(1, 1, True, 'Carrier')
# s2 = Ship(1, 1, False, 'Destroyer')
# for square in s1.squares:
#     print(square.x, square.y)
# for square in s2.squares:
#     print(square.x, square.y)
# print(s1.is_sunk())
# for square in s1.squares:
#     square.change_status_to_hit()
# print(s1.is_sunk())
#
# o = Ocean("player1")
# p = Ocean("player2")
# o.add_ship(1, 1, True, 'Carrier')
# o.add_ship(4, 7, False, 'Destroyer')
# o.print_ocean("player1")
# o.print_ocean("player2")


# test = Player("abc")
# test.print_ocean()
