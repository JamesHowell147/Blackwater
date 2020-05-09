#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from colorama import init, Fore
import sys
from time import sleep

init()


def write(string, color="", type_speed = 0.015):
    if color == "dark grey":
        sys.stdout.write('\33[1m' + Fore.BLACK)
    elif color == "black":
        sys.stdout.write('\33[2m' + Fore.BLACK)
    elif color == "red":
        sys.stdout.write('\33[1m' + Fore.RED)
    elif color == "dark red":
        sys.stdout.write('\33[2m' + Fore.RED)
    elif color == "green":
        sys.stdout.write('\33[1m' + Fore.GREEN)
    elif color == "dark green":
        sys.stdout.write('\33[2m' + Fore.GREEN)
    elif color == "yellow":
        sys.stdout.write('\33[1m' + Fore.YELLOW)
    elif color == "dark yellow":
        sys.stdout.write('\33[2m' + Fore.YELLOW)
    elif color == "blue":
        sys.stdout.write('\33[1m' + Fore.BLUE)
    elif color == "dark blue":
        sys.stdout.write('\33[2m' + Fore.BLUE)
    elif color == "magenta":
        sys.stdout.write('\33[1m' + Fore.MAGENTA)
    elif color == "dark magenta":
        sys.stdout.write('\33[2m' + Fore.MAGENTA)
    elif color == "cyan":
        sys.stdout.write('\33[1m' + Fore.CYAN)
    elif color == "dark cyan":
        sys.stdout.write('\33[2m' + Fore.CYAN)
    elif color == "white":
        sys.stdout.write('\33[1m' + Fore.WHITE)
    else:  #Light Grey
        sys.stdout.write('\33[2m' + Fore.WHITE)

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
