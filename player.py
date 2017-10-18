import random

from ocean import Ocean
from square import Square


class Player():

    def __init__(self, name):
        self.name = name
        self.ocean = Ocean(self)
        #self.ships = []

    def is_winner(self, other):
        other_ocean = other.get_ocean()
        for ship in other_ocean.get_ships():
            if not ship.is_sunk():
                return False
        return True

    # def add_ships(self):
        # self.ocean...
        # zamienienie pustych kwadratów
        # na kwadraty będące częścią statków
        # pieciu rodzajów
        # pass

    def get_ocean(self):
        return self.ocean

    def get_name(self):
        return self.name

    def shoot(self, other, x, y):

        ocean = other.get_ocean()
        square = ocean.ocean[y][x]
        if square.get_status() == Square.SQUARE_STATES['empty']:
            square.change_status_to_missed()
        elif square.get_status() == Square.SQUARE_STATES['ship']:
            square.change_status_to_hit()
        elif square.get_status == Square.SQUARE_STATES['hit']:
            return False
        elif square.get_status == Square.SQUARE_STATES['missed']:
            return False

        return True


class ComputerPlayer(Player):

    def __init__(self, difficulty_level):
        super().__init__(name='Computer')
        self.difficulty_level = difficulty_level

    def shoot(self, other):
        x = random.randrange(Ocean.width)
        y = random.randrange(Ocean.height)

        if level == 'easy':
            super().shoot(other, x, y)

        if level == 'medium':
            super().shoot(other, x, y)
            super().shoot(other, x, y)

        if level == 'hard':
            ocean = other.ocean
            if random.randint(1, 100) % 3 == 0:
                for row in ocean:
                    for square in row:
                        if square == Square.SQUARE_STATES['ship']:
                            Square.change_status_to_hit()
                    break
            else:
                super().shoot(other, x, y)

    def add_ships(self):
        pass

