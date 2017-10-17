from square import Square
from ship import Ship

class Ocean():

    width = 10
    heigth = 10

    def __init__(self, owner):

        self.ocean = []
        self.owner = owner

        for y in range(1, 11):
            row = []
            for x in range(1, 11):
                row.append(Square(x, y, Square.get_status_empty()))
            self.ocean.append(row)

    def is_ship_on_board(self, ship):
        for square in ship.squares:
            if square.get_x not in range(1, self.width + 1):
                return False
            if square.get_y not in range(1, self.height + 1):
                return False
        return True

    def add_ship(self, x, y, is_horizontal, ship_type):
        ship = Ship(x, y, is_horizontal, ship_type)

        is_ship_on_board(ship)
        is_ship_on_emty_spaces(ship)
        is_ship_not_touching_other_ships(ship)

    def print_ocean(self, player): # dodac atrybut player1
        coordinates = ('  ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
        print("   ".join(coordinates))
        for index, y in enumerate(range(10)):
            print(str(index + 1).rjust(2) + " | ", end="")
            for x in range(10):
                if player != self.owner and self.ocean[y][x] == "@":
                    self.ocean[y][x] = " "
                else:
                    print(self.ocean[y][x], end=" | ")

            print("\n" + "--------------------------------------------")

o = Ocean("player1")
p = Ocean("player2")
p.print_ocean(o)
o.print_ocean(p)
