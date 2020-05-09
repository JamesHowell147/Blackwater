import sys
from time import sleep


def write(string, color="", type_speed = 0.015):
    word_list = string.split(" ")
    line_length = 0
    for word in word_list:
        word_length = len(word)
        if line_length + word_length < 79:
            line_length += word_length + 1
            for character in word:
                sleep(type_speed)
                sys.stdout.write(character)
                sys.stdout.flush()
        else:
            line_length = word_length
            new_line()
            for character in word:
                sleep(type_speed)
                sys.stdout.write(character)
                sys.stdout.flush()
        sys.stdout.write(" ")
        sys.stdout.flush()


def new_line():
    sys.stdout.write('\n')
