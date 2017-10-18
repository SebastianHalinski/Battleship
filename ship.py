from square import Square


class Ship():

    SHIP_TYPE_TO_LENGTH = {'Carrier': 5,
                           'Battleship': 4,
                           'Cruiser': 3,
                           'Submarine': 3,
                           'Destroyer': 2}

    def __init__(self, x, y, is_horizontal, ship_type):
        self.x = x
        self.y = y
        self.ship_type = ship_type
        self.is_horizontal = is_horizontal
        self.length = self.SHIP_TYPE_TO_LENGTH[ship_type]

    def get_territory(self):
        '''Returns coordinates of ship in form of set of tuples of x, y'''

        ship_territory = set()

        if self.is_horizontal:
            for i in range(self.length):
                ship_territory.add((self.x + i, self.y))

        else:
            for i in range(self.length):
                ship_territory.add((self.x, self.y + i))

        return ship_territory

    def get_region(self):
        '''Returns coordinates of ship and its surroundings in form of set of tuples of x, y'''

        ship_region = set()
        ship_territory = self.get_territory()

        for i, j in ship_territory:
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    ship_region.add((x, y))

        return ship_region

    def is_sunk(self, board):

        ship_territory = self.get_territory()
        for x, y in ship_territory:
            square = board[y][x]
            if square.get_status() == Square.SQUARE_STATES['ship']:
                return False

        return True
