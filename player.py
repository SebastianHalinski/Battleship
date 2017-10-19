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
        ''' CHanges status of hit square on enemy's board.
        Returns True if location was not hit before, else None'''

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

    @staticmethod
    def get_surroundings(x, y):

        surroundings = set()

        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if (i, j) != (x, y) and i in range(Ocean.width) and j in range(Ocean.height):
                    surroundings.add((i, j))

        return surroundings

    @staticmethod
    def get_horizontal_neighbours(x, y):
        neighbours = set()

        for i in (x - 1, x + 1):
            if i in range(Ocean.width):
                neighbours.add((i, y))

        return neighbours

    @staticmethod
    def get_vertical_neighbours(x, y):
        neighbours = set()

        for j in (y - 1, y + 1):
            if j in range(Ocean.width):
                neighbours.add((x, j))

        return neighbours

    def choose_random_shot(self):
        x = random.randrange(Ocean.width)
        y = random.randrange(Ocean.height)

        while (x, y) in self.do_not_shoot:
            x = random.randrange(Ocean.width)
            y = random.randrange(Ocean.height)

        return x, y

    def get_is_horizontal(self):
        x_index = 0
        y_index = 1

        x_values = []
        y_values = []
        for hit in self.unsunk_hits:
            x = hit[x_index]
            y = hit[y_index]
            x_values.append(x)
            y_values.append(y)

        if len(set(y_values)) == 1:
            return True
        else:
            return False

    def choose_shot(self):
        if self.difficulty_level == 'EASY':
            shot = self.choose_random_shot()
            return shot

        elif self.difficulty_level == 'MEDIUM':
            if self.unsunk_hits:
                for hit in self.unsunk_hits:
                    surroundings = ComputerPlayer.get_surroundings(*hit)
                    for shot in surroundings:
                        if shot not in self.do_not_shoot:
                            return shot
            else:
                shot = self.choose_random_shot()
                return shot

        elif self.difficulty_level == 'HARD':
            if self.unsunk_hits:
                if len(self.unsunk_hits) > 1:
                    for hit in self.unsunk_hits:
                        is_horizontal = self.get_is_horizontal()
                        if is_horizontal:
                            neighbours = ComputerPlayer.get_horizontal_neighbours(*hit)
                            for shot in neighbours:
                                if shot not in self.do_not_shoot:
                                    return shot
                        else:
                            neighbours = ComputerPlayer.get_vertical_neighbours(*hit)
                            for shot in neighbours:
                                if shot not in self.do_not_shoot:
                                    return shot

                else:
                    for hit in self.unsunk_hits:
                        neighbours = ComputerPlayer.get_horizontal_neighbours(*hit)
                        neighbours.update(ComputerPlayer.get_vertical_neighbours(*hit))
                        for shot in neighbours:
                            if shot not in self.do_not_shoot:
                                return shot
            else:
                shot = self.choose_random_shot()
                return shot

    def mark_ship_region_as_do_not_shoot(self, ship):
        self.do_not_shoot.extend(ship.get_region())
        self.unsunk_hits.clear()

    def shoot(self, other, x, y):
        other_ocean = other.get_ocean()
        other_board = other_ocean.get_board()
        square = other_board[y][x]
        if square.get_status() == Square.SQUARE_STATES['empty']:
            square.set_status('missed')

        elif square.get_status() == Square.SQUARE_STATES['ship']:
            square.set_status('hit')

            ship = self.get_ship_from_coordinates(other, x, y)
            if ship.is_sunk(other_board) and self.difficulty_level != 'E':
                self.mark_ship_region_as_do_not_shoot(ship)
            else:
                self.unsunk_hits.append((x, y))

        self.do_not_shoot.append((x, y))
