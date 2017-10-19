import random

from ocean import Ocean
from square import Square


class Player():

    def __init__(self, name):
        self.name = name
        self.ocean = Ocean(name)

    def get_ocean(self):
        return self.ocean

    def get_name(self):
        return self.name

    def is_winner(self, other):
        ''' Returns True if all ships on enemy's board are sunk, else False'''

        other_ocean = other.get_ocean()
        other_ships = other_ocean.get_ships()
        other_board = other_ocean.get_board()
        for ship in other_ships:
            if not ship.is_sunk(other_board):
                return False
        return True

    def shoot(self, other, x, y):

        ocean = other.get_ocean()
        square = ocean.board[y][x]
        if square.get_status() == Square.SQUARE_STATES['empty']:
            print('You missed!!!')
            square.set_status('missed')
            return True
        elif square.get_status() == Square.SQUARE_STATES['ship']:
            print('Hit!!!')
            square.set_status('hit')
            return True

    def get_ship_from_coordinates(self, other, x, y):
        ''' If square at location x, y on enemy's board is a part of a ship it returns that ship.
        Else return None'''

        other_ocean = other.get_ocean()
        other_ships = other.ocean.get_ships()
        for ship in other_ships:
            ship_territory = ship.get_territory()
            if (x, y) in ship_territory:
                return ship


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

    @staticmethod
    def get_surroundings(x, y):

        surroundings = set()

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i, j) != (x, y) and i in range(Ocean.width) and j in range(Ocean.height):
                    surroundings.add((x, y))

        return surroundings

    def choose_shot(self):
        if unsunk_hits:
            for hit in self.unsunk_hits:
                surroundings = get_surroundings(*hit)
                for shot in surroundings:
                    if shot not in self.do_not_shoot:
                        return shot

        else:
            x = random.randrange(Ocean.width)
            y = random.randrange(Ocean.height)
            while (x, y) in self.do_not_shoot:
                x = random.randrange(Ocean.width)
                y = random.randrange(Ocean.height)
            return x, y

    def mark_ship_territory_as_do_not_shoot(self):
        #self.unsunk_hits.sort()
        pass

    def shoot(self, other, x, y):

        ocean = other.get_ocean()
        square = ocean.board[y][x]
        if square.get_status() == Square.SQUARE_STATES['empty']:
            square.set_status('missed')
            self.do_not_shoot.append(x, y)
        elif square.get_status() == Square.SQUARE_STATES['ship']:
            square.set_status('hit')
            ship = self.get_ship_from_coordinates(other, x, y)
            if square.ship.is_sunk():
                self.move_ship_territory_to_do_not_shoot(ship)
            else:
                self.unsunk_hits.append(x, y)

        return True

    def add_ships(self):
        pass
