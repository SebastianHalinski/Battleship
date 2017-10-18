import random
from ocean import Ocean

class Player():

    def __init__(self, name):
        self.name = name
        self.ocean = Ocean(name) # init ocean
        self.ships = []

    def is_winner(self, other):
        # other bo plansza przeciwnika
        for ship in other.ships:
            if ship is not is_sunk():
                return False
        return True

    #def add_ships(self):
        # self.ocean...
        # zamienienie pustych kwadratów
        # na kwadraty będące częścią statków
        # pieciu rodzajów
        #pass

    def shoot(self, other, location):
        # zamienianie lokacji A6 na x, y
        # ta część może jako metoda statyczna?

        # zmienianie statusu tej lokacji
        # na planszy przeciwnika
        x_cords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        y = location[1]
        for i in x_cords:
            if location[0] == i:
                x = int(x_cords.index(i)) + 1

        ocean = other.ocean
        square = ocean(x, y)
        if square.get_status() == Square.SQUARE_STATES['empty']:
            Square.change_status_to_missed()
        elif square.get_status() == Square.SQUARE_STATES['ship']:
            Square.change_status_to_hit()
        elif square.get_status == Square.SQUARE_STATES['hit']:
            return False
        elif square.get_status == Square.SQUARE_STATES['missed']:
            return False
        return True


class ComputerPlayer(Player):

    def __init__(self, difficulty_level):
        super().__init__(name='Computer')
        self.difficulty_level = difficulty_level

    def shoot(self, other, level):

        def transform_cords_to_location():
            x_cords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
            y_location = random.randrange(1, 11)
            x_location = random.choice(x_cords)
            location = str(y_location) + str(x_location)
            return location

        if level == 'easy':
            location = transform_cords_to_location()
            super().shoot(other, location)

        if level == 'medium':
            location = transform_cords_to_location()
            super().shoot(other, location)
            location = transform_cords_to_location()
            super().shoot(other, location)

        if level == 'hard':
            ocean = other.ocean
            if random.randint(1, 100) % 3 == 0:
                for row in ocean:
                    for square in row:
                        if square == Square.SQUARE_STATES['ship']:
                            Square.change_status_to_hit()
                    break
            else:
                location = transform_cords_to_location()
                super().shoot(other, location)

    def add_ships(self):
        pass

test = Player("abc")
test.ocean.print_ocean()
