from square import Square
from ship import Ship
# from player import Player


class Ocean():

    width = 10
    height = 10

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
            if square.get_x() not in range(1, self.width + 1):
                return False
            if square.get_y() not in range(1, self.height + 1):
                return False
        return True

    def is_ship_location_valid(self, ship):
        ship_territory = []

        for square in ship.squares:
            x = square.get_x()
            y = square.get_y()

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if i in range(1, self.width + 1) and j in range(1, self.height + 1) and (i, j) not in ship_territory:
                        ship_territory.append(tuple([i, j]))

        for coordinate in ship_territory:
            x, y = coordinate
            square = self.ocean[y][x]
            if square.get_status() != Square.get_status_empty():
                return False

        return True

    def add_ship(self, x, y, is_horizontal, ship_type):
        ship = Ship(x, y, is_horizontal, ship_type)

        if self.is_ship_on_board(ship) and self.is_ship_location_valid(ship):
            for square in ship.squares:
                x = square.get_x()
                y = square.get_y()
                self.ocean[y - 1][x - 1] = square
            return True
        else:
            return False

    def print_ocean(self, player):
        coordinates = ('  ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
        print("Player name: " + self.owner + "\n")
        print("   ".join(coordinates))

        for index, y in enumerate(range(10)):

            print(str(index + 1).rjust(2) + " | ", end="")

            for x in range(10):
                square = self.ocean[y][x]
                if player != self.owner and square.get_status() == "@":
                    print(" ", end=" | ")
                else:
                    print(square, end=" | ")

            print("\n" + "--------------------------------------------")


o = Ocean("player1")
p = Ocean("player2")
o.add_ship(1, 1, True, 'Carrier')
o.add_ship(4, 7, False, 'Destroyer')
o.print_ocean("player1")
o.print_ocean("player2")
