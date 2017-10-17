from square import Square


class Ship():

    def is_sunk(self):
        for square in self.squares:
            if square.get_status() == Square.get_status_ship():
                return False
        return True


class Carrier(Ship):
    length = 5

    def __init__(self, x, y, is_horizontal):
        # self.x = x
        # self.y = y
        # self.is_horizontal = is_horizontal
        self.squares = []
        if is_horizontal:
            for i in range(self.length):
                self.squares.append(Square(x, y, Square.get_status_ship()))
                x += 1
        else:
            for i in range(self.length):
                self.squares.append(Square(x, y, Square.get_status_ship()))
                y += 1


class Battleship(Ship):
    length = 4


class Cruiser(Ship):
    length = 3


class Submarine(Ship):
    length = 3


class Destroyer(Ship):
    length = 2


s1 = Carrier(1, 1, True)
s2 = Carrier(1, 1, False)
for square in s1.squares:
    print(square.x, square.y)
for square in s2.squares:
    print(square.x, square.y)
print(s1.is_sunk())
for square in s1.squares:
    square.change_status_to_hit()
print(s1.is_sunk())


# może by tutaj już dać żeby nie wychodziło poza
# a zachodzenie na inne i  dotykanie dać do ocean?


# init taki sam dla wszystkich podklas więc może
# zrobić tylko klasę ship i dodatkowo nazwę i długość?
# można by dodać atrybut klasy: słownik(nazwa: length)

# żeby Ship był abstrakcyjny, musi mieć jedną abstrakcyjną metodę

# ustalić jak x i y