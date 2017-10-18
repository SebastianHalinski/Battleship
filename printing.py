import os


def read_screen(file_name):
    with open(file_name) as file:
        contents = file.read()
    return contents


def print_waiting_screen(file_name):
    #os.system('clear')
    if file_name == "waiting_for_player_1.txt":
        waiting_screen_1 = read_screen(file_name)
        print(waiting_screen_1)
        input('Press enter to continue: ')

    elif file_name == "waiting_for_player_2.txt":
        waiting_screen_2 = read_screen("waiting_for_player_2.txt")
        print(waiting_screen_2)
        input('Press enter to continue: ')


def print_starting_screen():
    os.system('clear')
    introduction_screen = read_screen('intro.txt')
    print(introduction_screen)
    input('Press enter to continue: ')


def print_how_to_play():
    os.system('clear')
    how_to_play_screen = read_screen('how_to_play.txt')
    print(how_to_play_screen)
    input('Press enter to quit: ')


def print_hall_of_fame():
    os.system('clear')
    contents = []
    with open('high_scores.txt') as file:
        for line in file:
            sublist = line.strip().split(',')
            contents.append(sublist)
    print('\n\n\n\n')
    print("HALL OF FAME:\n\n")
    print('NAME'.rjust(10), 'SCORE'.ljust(10))
    for sublist in contents:
        print(sublist[0].rjust(10), end=' ')
        print(sublist[1].ljust(10))
    print('\n')
    input('Press enter to quit: ')



def print_win_screen():
    #os.system('clear')
    win_screen = read_screen('you_win.txt')
    print(win_screen)
    input('Press enter to continue: ')

def print_lose_screen():
    #os.system('clear')
    lose_screen = read_screen('you_lose.txt')
    print(lose_screen)
    input('Press enter to continue: ')
