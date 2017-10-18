from ship import Ship
from square import Square


class Ocean():

    width = 10
    height = 10

    def __init__(self, owner):

        self.board = []
        self.ships = []
        self.owner = owner

        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Square(x, y, Square.SQUARE_STATES['empty']))
            self.board.append(row)

    def get_ships(self):
        return self.ships

    def get_board(self):
        return self.board

    def is_ship_on_board(self, ship):
        '''Return True if ship will fit on board, else False'''

        ship_territory = ship.get_territory()

        for x, y in ship_territory:
            if x not in range(self.width):
                return False
            if y not in range(self.height):
                return False
        return True

    def is_ship_location_valid(self, ship):
        '''Return True if ship will not overlap or touch other ships, else False'''

        ship_region = ship.get_region()

        for x, y in ship_region:
            try:
                square = self.board[y][x]
            except IndexError:
                pass
            else:
                if square.get_status() == Square.SQUARE_STATES['ship']:
                    return False

        return True

    def add_ship(self, x, y, is_horizontal, ship_type):
        ''' Tries to add ship to board. Returns True if ship has been added to board, else False'''

        ship = Ship(x, y, is_horizontal, ship_type)
        ship_territory = ship.get_territory()

        if self.is_ship_on_board(ship) and self.is_ship_location_valid(ship):
            for x, y in ship_territory:
                square = self.board[y][x]
                square.set_status('ship')
            self.ships.append(ship)
            return True

        else:
            return False

    def print_ocean(self, player):
        '''If player is the owner of the ocean prints board with all ships,
        else board with only hit squares of ships'''

        coordinates = ('  ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J')
        print("This board belongs to: " + self.owner + "\n")
        print("   ".join(coordinates))
        print("--------------------------------------------")

        for y in range(self.height):
            print(str(y + 1).rjust(2) + " | ", end="")

            for x in range(self.width):
                square = self.board[y][x]
                if player != self.owner and square.get_status() == Square.SQUARE_STATES['ship']:
                    print(" ", end=" | ")
                else:
                    print(square, end=" | ")

            print("\n" + "--------------------------------------------")
