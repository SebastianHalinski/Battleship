from ocean import Ocean
from player import ComputerPlayer, Player
from ship import Ship
from square import Square


def conver_location_to_coordinates(location):
    y = int(location[1]) - 1

    x_cords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for i in x_cords:
        if location[0] == i:
            x = int(x_cords.index(i))

    return x, y


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

s1 = Ship(1, 1, True, 'Carrier')
s2 = Ship(1, 1, False, 'Destroyer')
for square in s1.squares:
    print(square.x, square.y)
for square in s2.squares:
    print(square.x, square.y)
print(s1.is_sunk())
for square in s1.squares:
    square.change_status_to_hit()
print(s1.is_sunk())

o = Ocean("player1")
p = Ocean("player2")
o.add_ship(1, 1, True, 'Carrier')
o.add_ship(4, 7, False, 'Destroyer')
o.print_ocean("player1")
o.print_ocean("player2")


# test = Player("abc")
# test.print_ocean()
