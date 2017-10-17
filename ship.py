from square import Square


class Ship():

    SHIP_TYPE_TO_LENGTH = {'Carrier': 5,
                           'Battleship': 4,
                           'Cruiser': 3,
                           'Submarine': 3,
                           'Destroyer': 2}

    def __init__(self, x, y, is_horizontal, ship_type):
        # self.x = x
        # self.y = y
        # self.is_horizontal = is_horizontal

        # self.ship_type = ship_type

        self.length = self.SHIP_TYPE_TO_LENGTH[ship_type]
        self.squares = []

        if is_horizontal:
            for i in range(self.length):
                self.squares.append(Square(x, y, Square.get_status_ship()))
                x += 1
        else:
            for i in range(self.length):
                self.squares.append(Square(x, y, Square.get_status_ship()))
                y += 1

    def is_sunk(self):
        for square in self.squares:
            if square.get_status() == Square.get_status_ship():
                return False
        return True

