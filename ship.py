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
        self.is_horizontal = is_horizontal
        # self.ship_type = ship_type
        self.length = self.SHIP_TYPE_TO_LENGTH[ship_type]

    def get_territory(self):
        ship_territory = set()

        if self.is_horizontal:
            for i in range(self.length):
                ship_territory.add((self.x + i, self.y))

        else:
            for i in range(self.length):
                ship_territory.add((self.x, self.y + i))

        return ship_territory

    def get_region(self):
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
            if square.get_status() == Square.get_status_ship():
                return False
                
        return True
