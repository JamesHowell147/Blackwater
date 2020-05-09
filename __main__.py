import starting_screen
import navigation
import command_parser
import items
import sys
from output import write, new_line

this = sys.modules[__name__]
command_parser.items = items
command_parser.navigation = navigation
items.command_parser = command_parser
items.navigation = navigation


def game_over(message):
    global exit
    write(message, "dark red")
    new_line()
    write("                                   GAME OVER", "red")
    new_line()
    input()
    quit()


def win_game():
    write("You try a few of the keys in the door...Ah, it fits! You turn the key in the lock and the door swings open. FREEDOM")
    new_line()
    new_line()
    write("                                    YOU WIN!", "green")
    new_line()
    new_line()
    write("Thanks for playing!", "green")
    new_line()
    input()
    quit()

command_parser.game_over = this.game_over
navigation.rooms["atrium"].win_game = this.win_game

while True:
    command_parser.execute_command(command_parser.get_input())
