class Player():

    def __init__(self, name):
        self.ocean  # init ocean
        self.ships = []

    def is_winner(self, other???):
        # other bo plansza przeciwnika
        for ship in other.ships:
            if not ship is_sunk():
                return False
        return True

    def add_ships(self):
        # self.ocean...
        # zamienienie pustych kwadratów
        # na kwadraty będące częścią statków
        # pieciu rodzajów
        pass

    def shoot(self, location):
        # zamienianie lokacji A6 na x, y
        # ta część może jako metoda statyczna?

        # zmienianie statusu tej lokacji
        # na planszy przeciwnika
        x_cords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        y = location[1]
        for i in x_cords:
            if location[0] == i:
                x = int(x_cords.index(i)) + 1

        if Square.get_status() == Square.SQUARE_STATES['empty']:
            Square.change_status_to_missed()
        elif Square.get_status() == Square.SQUARE_STATES['hit']:
            Square.change_status_to_hit()
        elif Square.get_status == Square.SQUARE_STATES['hit']:
            return False
        elif Square.get_status == Square.SQUARE_STATES['missed']:
            return False


class ComputerPlayer(Player):

    def __init__(self, difficulty_level):
        super().__init__(name='Computer')
        self.difficulty_level = difficulty_level

    def shoot(self, level???):
        pass

    def add_ships(self):
        pass
