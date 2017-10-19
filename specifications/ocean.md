__ocean.py__

Class Ocean:

## ATTRIBUTES:
It has 2 default class attributes: 
width = 10
height = 10

They refer to the size of boards.

### METHODS:

* __init__(owner): the constructor of an ocean

* get_ships(): getter of instance attribute ship

* get_board(): getter of instance attribute board

* is_ship_on_board(ship): returns True if ship will fit on board, else False

* is_ship_location_valid(ship): returns True if ship will not overlap or touch other ships, else False

* add_ship(x, y, is_horizontal, ship_type): tries to add ship to board. Returns True if ship has been added to board, else False

* print_ocean(player): if player is the owner of the ocean prints board with all ships, else board with only hit squares of ships



