## Specification


__main.py__

Running main.py you will see the following menu: 

Press 1 to start multiplayer game
Press 2 to start singleplayer game
Press 0 to exit


1) Multiplayer game mode allows you to play the game with a friend. At the beggining the program asks users for their names. They also need to place their ships on the board. Then the players are going to guess the location of the opponent's ship. If all the opponent's ships are sunk you win!

2)In the single player game mode the computer is your opponent. The program asks the user for his/her name. The player also needs to place their ships on the board. If all the opponent's ships are sunk you win! Try to sink all the boats using as few "hits" as possible. If your score is among the highest ones you will join the other winners at the Hall of Fame.

0) By pressing 0 you can leave the program.


###Functions:

* high_score(level, shots): calculate and return player score


* add_shot(shots): count player guesses and return the result


* read_screen(file_name): imports screens from file and returns its contents


* print_screen(file_name): *print screens


* get_correct_locations(): protects from invalid inputs. Returns lists of correct locations.
    

* convert_location_to_coordinates(location): converts user input to x, y integers


* get_is_horizontal(): returns True if the ship is placed horizontally, False if vertically


* get_location() 


* human_add_ships(player): add ships on player board(ocean). 


* computer_add_ships(computer): randomly place ships on computer board

    
* set_up_player(): function create player object 


* human_turn(player, enemy): one turn of the game (used not only in multiplayer mode but also in singleplayer.


* computer_turn(computer_player, enemy): one computer turn of the game 


* multiplayer_game(): a main shell of multiplayer game


* single_game(): a main shell of single player game

