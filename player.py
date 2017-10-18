import random

from ocean import Ocean
from square import Square


class Player():

    def __init__(self, name):
        self.name = name
        self.ocean = Ocean(name)

    def is_winner(self, other):
        other_ocean = other.get_ocean()
        for ship in other_ocean.get_ships():
            if not ship.is_sunk(other.get_ocean().board):
                return False
        return True

    def get_ocean(self):
        return self.ocean

    def get_name(self):
        return self.name

    def shoot(self, other, x, y):

        ocean = other.get_ocean()
        square = ocean.board[y][x]
        if square.get_status() == Square.SQUARE_STATES['empty']:
            square.set_status('missed')
        elif square.get_status() == Square.SQUARE_STATES['ship']:
            square.set_status('hit')
        elif square.get_status == Square.SQUARE_STATES['hit']:
            return False
        elif square.get_status == Square.SQUARE_STATES['missed']:
            return False

        return True


class ComputerPlayer(Player):

    def __init__(self, difficulty_level):
        super().__init__(name='Computer')
        self.difficulty_level = difficulty_level
        self.do_not_shoot = []
        self.unsunk_hits = []

    # def shoot(self, other):
    #     x = random.randrange(Ocean.width)
    #     y = random.randrange(Ocean.height)

    #     if level == 'easy':
    #         super().shoot(other, x, y)

    #     if level == 'medium':
    #         super().shoot(other, x, y)
    #         super().shoot(other, x, y)

    #     if level == 'hard':
    #         ocean = other.ocean
    #         if random.randint(1, 100) % 3 == 0:
    #             for row in ocean:
    #                 for square in row:
    #                     if square == Square.SQUARE_STATES['ship']:
    #                         Square.change_status_to_hit()
    #                 break
    #         else:
    #             super().shoot(other, x, y)

    def choose_shot(self):
        pass

    def shoot(self, other, x, y):

        # ocean = other.get_ocean()
        # square = ocean.ocean[y][x]
        # if square.get_status() == Square.SQUARE_STATES['empty']:
        #     square.set_status('missed')
        #     self.do_not_shoot.append(x, y)
        # elif square.get_status() == Square.SQUARE_STATES['ship']:
        #     square.set_status('hit')
        #     ship =
        #     if square.ship.is_sunk():
        #         self.move_ship_territory_to_do_not_shoot(ship)
        #     else:
        #         self.unsunk_hits.append(x, y)

        # return True
        pass

    def add_ships(self):
        pass
