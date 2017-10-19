__player.py__

Class Player:

the class Player is a blueprint for creating players.

## METHODS

* __init__(name): constructor of player 

* get_ocean(): getter of instance attribute ocean

* get_name(): getter of instance attribute name

* is_winner(other): returns True if player has won, else False

* shoot(other, x, y): tries to shoot enemy ships, if the location has been shot before returns None, else returns True

* get_ship_from_coordinates(other, x, y): returns an object of ship if location is part of a ship, else None


Class ComputerPlayer(Player)

This class is a subclass inheriting from class Player.

## METHODS:

* __init__(difficulty_level): constructor of computer player

* @staticmethod: get_surroundings(x, y): returns a set containing the coordinates of surroundings of the location

* @staticmethod: get horizontal neighbours(x, y): returns the scope of horizontally adjacent  squares in the form of a set or tuple

* @staticmethod: get vertical neighbours(x, y): returns the scope of vertically adjacent squares in the form of a set of tuple

* choose_random_shot(): returns random location on board which was not hit before 

* get_is_horizontal(): returns True if ship is horizontal, else False

* choose_shot(): returns the location of next computer shot which depends on difficulty level

* mark_ship_region_as_do_not_shot(ship): moves locations of region of ship to list do_not_shoot and clears unsign hits list

* shoot(other, x, y): computer shooting


