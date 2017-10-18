from ship import Ship
from square import Square


class Ocean():

    width = 10
    height = 10

    def __init__(self, owner):

        self.owner = owner
        self.ocean = []
        self.ships = []

        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Square(x, y, Square.get_status_empty()))
            self.ocean.append(row)

    def get_ships(self):
        return self.ships

    def is_ship_on_board(self, ship):
        for square in ship.squares:
            if square.get_x() not in range(self.width):
                return False
            if square.get_y() not in range(self.height):
                return False
        return True

    def is_ship_location_valid(self, ship):
        ship_territory = set()

        for square in ship.squares:
            x = square.get_x()
            y = square.get_y()

            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if i in range(self.width) and j in range(self.height):
                        ship_territory.add((i, j))

        for coordinate in ship_territory:
            x, y = coordinate
            square = self.ocean[y][x]
            if square.get_status() == Square.get_status_ship():
                return False

        return True

    def add_ship(self, x, y, is_horizontal, ship_type):
        ship = Ship(x, y, is_horizontal, ship_type)

        if self.is_ship_on_board(ship) and self.is_ship_location_valid(ship):
            for square in ship.squares:
                x = square.get_x()
                y = square.get_y()
                self.ocean[y][x] = square
            self.ships.append(ship)
            return True

        else:
            return False

    def print_ocean(self):
        coordinates = ('  ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
        print("Player name: " + self.owner.get_name() + "\n")
        print("   ".join(coordinates))
        print("--------------------------------------------")

        for y in range(self.height):
            print(str(y + 1).rjust(2) + " | ", end="")

            for x in range(self.width):
                square = self.ocean[y][x]
                if player != self.owner and square.get_status() == Square.SQUARE_STATES['ship']:
                    print(" ", end=" | ")
                else:
                    print(square, end=" | ")

            print("\n" + "--------------------------------------------")
