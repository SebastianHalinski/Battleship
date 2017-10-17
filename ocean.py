from square import Square

class Ocean():

    def __init__(self):
        self.ocean = []
        for y in range(1, 11):
            row = []
            for x in range(1, 11):
                row.append(Square(x, y, Square.get_status_empty()))
            self.ocean.append(row)

        #list 10 list pustych kwadratów
        #tylko to będzie player.ocean.ocean


    # def add_ship(self, x, y, is_horizontal, ship_type):
    #     # init ship(x, y, is_horizontal)
    #     # sprawdzenie czy nie wystaje
    #     # czy nie zachodzi na inne statki
    #     # czy nie dotyka innych statków
    #
    #     # is_ship_on_board(ship)
    #     # is_ship_on_emty_spaces(ship)
    #     # is_ship_not_touching_other_ships(ship)
    #
    #def print_ocean(player):
    #     if player is owner:
    #         pass
    #     else:
    #         pass

o = Ocean()
print(o)
