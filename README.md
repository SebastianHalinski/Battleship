# Battleship in the OOP way


## The story
	The pirate called Jack Crow is looking for somebody to create a program which will help him to train candidates who want to join his crew. Our idea is the Battleship game. 

The object of the Battleship is to try and sink all of the other player's before they sink all of your ships. All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  The other player also tries to hit your ships by calling out coordinates.  Neither you nor the other player can see the other's board so you must try to guess where they are.


## Specification


__main.py__

Running main.py you will see the following menu: 

Press 1 to start multiplayer game
Press 2 to start singleplayer game
Press 3 to learn how to play
Press 4 to see the Hall of Fame
Press 0 to exit


1) Multiplayer game mode allows you to play the game with a friend. At the beggining the program asks users for their names. They also need to place their ships on the board. Then the players are going to guess the location of the opponent's ship. If all the opponent's ships are sunk you win!

2)In the single player game mode the computer is your opponent. The program asks the user for his/her name. The player also needs to place their ships on the board. If all the opponent's ships are sunk you win! Try to sink all the boats using as few "hits" as possible. If your score is among the highest ones you will join the other winners at the Hall of Fame.

3) How to play option helps you to understand the game's rules importing them from a file.

4) Hall of Fame option allows you to see the table with the highest scores.

0) By pressing 0 you can leave the program.


###Functions:
* press_enter_to_continue():


* read_screen(file_name): imports screens from file and returns its contents


* print_screen(file_name): *print screens


* get_correct_locations():
    

* convert_location_to_coordinates(location):


* get_is_horizontal(): returns True if the ship is placed horizontally, False if vertically


* get_location()


* add_ships(player):
    
* set_up_player():

* human_turn(player, enemy): one turn of the game (used not only in multiplayer mode but also in singleplayer.
        
* multiplayer_game():



__square.py__


Class Square 

The Square class represents one single location (square) of the board.

## ATTRIBUTE:

*SQUARE_STATES: a dicionary representing four types of symbols appearing on the board:
'empty': ' ', 'ship': '@','hit': 'X','missed': 'O'

### METHODS:

* __init__(x,  y,  status): returns  None
* __str__(): returns status as a str
* get_x():returns int
* get_y(): returns int
* get_status(): returns str
* set_status(): returns str


__ship.py__

Class Ship:

## ATTRIBUTE:

SHIP_TYPE_TO_LENGTH is a dictionary containings names of ships as keys and their length:'Carrier': 5, 'Battleship': 4,'Cruiser': 3,'Submarine': 3,'Destroyer': 2

###METHODS: 
* __init__( x, y, is_horizontal, ship_type) allows to create ships of different type and location(horizontal or vertical)
* get_territory(): Returns coordinates of ship in form of set of tuples of x, y
* get_region(): Returns coordinates of ship and its surroundings in form of set of tuples of x, y
* is_sunk(board): Returns a bool value 



__ocean.py__
Class Ocean:

## ATTRIBUTES:
It has 2 default class attributes: 
width = 10
height = 10

They refer to the size of boards.

### METHODS:
* __init__(owner): None
* get_ships(): list
* get_board(): list
* is_ship_on_board(ship): returns True if ship will fit on board, else False
* is_ship_location_valid(ship): returns True if ship will not overlap or touch other ships, else False
* add_ship(x, y, is_horizontal, ship_type): tries to add ship to board. Returns True if ship has been added to board, else False
* print_ocean(player)if player is the owner of the ocean prints board with all ships, else board with only hit squares of ships


+ print_ocean(player)

__player.py__

Class Player:

the class Player is a blueprint for creating players.

## METHODS

* __init__(name): returns  None
* get_ocean(): returns object
* get_name(): returns str
* is_winner(other): returns bool
* shoot(other, x, y): returns bool
* get_ship_from_coordinates(other, x, y): returns a tuple containing 2 integers


Class ComputerPlayer(Player)
This class is a subclass inherits from class Player.

## METHODS:
* __init__(difficulty_level): returns None
*@staticmethod: get_surroundings(x, y): returns a set containing the coordinates of surrondings
* choose_shot(): returns 2 integers 
* shoot(other, x, y): returns bool










