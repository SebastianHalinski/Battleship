__ship.py__

Class Ship:

## ATTRIBUTE:

SHIP_TYPE_TO_LENGTH is a dictionary containing names of ships as keys and their length as values:'Carrier': 5, 'Battleship': 4,'Cruiser': 3,'Submarine': 3,'Destroyer': 2

###METHODS: 

* __init__( x, y, is_horizontal, ship_type) allows to create ships of different type and location(horizontal or vertical)

* get_territory(): Returns coordinates of ship in form of set of tuples of x, y

* get_region(): Returns coordinates of ship and its surroundings in form of set of tuples of x, y

* is_sunk(board): Returns True if ship is sunk and else if it isn't


