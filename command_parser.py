#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from output import write, new_line

game_over = None

character_substitutions = {
    "_": " ",
    "@": "a",
    "$": "s",
    "£": "e",
    "¥": "y",
    "€": "e",
    "¢": "c",
    "0": "o",
    "1": "l",
    "2": "z",
    "3": "e",
    "4": "a",
    "5": "s",
    "7": "t",
    "8": "b"
}

verbs = {
    "inspect": ["look", "check", "read", "examine"],
    "move": ["shift", "open", "push", "pull", "turn", "twist", "remove", "slide"],
    "go": ["enter", "walk", "run", "sprint", "sneak", "creep"],
    "take": ["grab", "pocket", "pick", "pickup", "snatch"],
    "put": ["place", "set"],
    "nothing": ["nill", "quit", "back", "undo"],
    "wear": ["wear", "equip"],
    "inventory": ["inv", "pack", "backpack", "bag", "pocket", "pockets", "storage"],
    "consume": ["drink", "eat", "swallow"]
}


def invalid_command(command):
    command = command.split(" ")
    if command == [""]:
        write("You can't do that at the moment.", "red")
        new_line()
        return
    if command[0] == "inspect":
        if len(command) == 1:
            write("You can't see one of those anywhere.", "red")
            new_line()
            return
        if len(command) == 2:
            write("You can't see the " + command[1] + " right now.", "red")
            new_line()
            return
        write("You can't see that right now.", "red")
        new_line()
        return
    if command[0] == "consume":
        if len(command) == 1:
            write("You can't see one of those anywhere.", "red")
            new_line()
            return
        if len(command) == 2:
            write("You can't eat the " + command[1] + ".", "red")
            new_line()
            return
        write("You can't eat that.", "red")
        new_line()
        return
    if command[0] == "wear":
        if len(command) == 1:
            write("You can't see one of those anywhere.", "red")
            new_line()
            return
        if len(command) == 2:
            write("You can't wear the " + command[1] + "!", "red")
            new_line()
            return
        write("You can't do that.", "red")
        new_line()
        return
    if command[0] == "move":
        if len(command) == 1:
            write("You can't get see one of those anywhere.", "red")
            new_line()
            return
        if len(command) == 2:
            write("You can't move the " + command[1] + ".", "red")
            new_line()
            return
        write("You can't move that.", "red")
        new_line()
        return
    if command[0] == "go":
        if len(command) == 1:
            write("You can't go there.", "red"),
            new_line()
            return
        if len(command) == 2:
            write("You can't go to the " + command[1] + ".", "red")
            new_line()
            return
        write("You can't go there.", "red")
        new_line()
        return
    if command[0] == "take":
        if len(command) == 1:
            write("You see one of those anywhere...", "red"),
            new_line()
            return
        if len(command) == 2:
            write("You can't take the " + command[1] + ".", "red")
            new_line()
            return
        write("You can't take that.", "red")
        new_line()
        return
    if command[0] == "put":
        if len(command) == 1:
            write("You don't see one of those anywhere...", "red"),
            new_line()
            return
        if len(command) == 2:
            write("Where do you want to put the " + command[1] + "?", "dark yellow")
            new_line()
            execute_command("put " + command[1] + " " + get_input())
            return
        if len(command) == 3:
            write("You can't put the " + command[1] + " on the " + command[2] + ".", "red")
            new_line()
            return
        write("You can't do that.", "red")
        new_line()
        return
    write("You can't do that.", "red")
    new_line()


def get_input():
    user_input = ""
    while user_input == "":
        write("> ")
        user_input = raw_input().lower()
        user_input = remove_punctuation(user_input)
        user_input = user_input.strip()
    return cull_words(user_input)


def remove_punctuation(user_input):
    processed_string = ""
    for c in user_input:
        if c in character_substitutions:
            processed_string += character_substitutions[c]
        elif c.isalpha() or c == " ":
            processed_string += c
    return processed_string


def substitute_words(word, dictionary):
    for entry in dictionary:
        if word == entry or word in dictionary[entry]:
            return entry
    return False


def cull_words(user_input):
    word_list = user_input.split(" ")
    key_words = ""
    for word in word_list:
        sub = substitute_words(word, navigation.current_room.objects)
        if sub:
            key_words += sub + " "
            continue
        sub = substitute_words(word, verbs)
        if sub:
            key_words += sub + " "
            continue
        inventory_sub_dictionary = {}
        for item in items.inventory:
            inventory_sub_dictionary[item] = items.item_list[item]
        sub = substitute_words(word, inventory_sub_dictionary)
        if sub in items.inventory:
            key_words += sub + " "
    if(len(key_words) == 0):
        return ""
    return key_words[:-1]


def execute_command(user_input):
    if user_input == "inventory":
        items.print_inventory()
        return
    for item in items.inventory:
        for command in items.item_commands[item]:
            if user_input == command:
                for action in items.item_commands[item][command]:
                    action()
                return
    for state in navigation.current_room.states:
        if navigation.current_room.states[state][0]:
            for command in navigation.current_room.states[state][1]:
                if user_input == command:
                    for action in navigation.current_room.states[state][1][command]:
                        action()
                    return
    for command in navigation.current_room.commands:
        if user_input == command:
            for action in navigation.current_room.commands[command]:
                action()
            return
    invalid_command(user_input)
