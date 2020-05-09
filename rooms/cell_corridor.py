#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from output import write, new_line
from items import pickup, drop, inventory
import command_parser

name = "cell corridor"

first_description = "You walk out into the main corridor of cells." 
#Description given when you first enter the room.

previously_entered = False #Keeps track of if the player has entered the room previously.

objects = { #Every possible object in the room and synonyms.
    "walls": ["wall"],
    "table": ["bench", "worktop", "desk", "bar", "workbench", "worktable"],
    "door": ["entrance", "doorway", "hatch", "exit", "back", "doors"],
    "window": ["opening", "bars", "hatch"],
    "floor": ["ground", "flooring"],
    "ceiling": ["roof"],
    "room": ["around"],
    "paper": ["note-2"],
    "radio": ["stereo", "player"],
    "guard": ["officer"],
    "inmates": ["prisoners", "patients", "captives"],
    "bulb": ["light", "lightbulb"],
    "cells": ["cell"],
    "book": ["books"]
}

states = {  #Used to add or overwrite commands when the state of the room changes.
    "paper taken": [
        False, {
            "inspect paper": [
                lambda: write("You've already picked up the paper."),
                lambda: new_line(),
            ],
            "take paper": [
                lambda: write("You've already picked up the paper."),
                lambda: new_line(),
            ],
            "inspect book": [
                lambda: write("The book contains nothing else of interest."),
                lambda: new_line()
            ],
            "take book": [
                lambda: write("You've already taken the book."),
                lambda: new_line()
            ]
        }
    ],
    "book taken": [
        False, {
            "inspect book": [
                lambda: write("The book contains nothing else of interest."),
                lambda: new_line()
            ],
            "take book": [
                lambda: write("You've already taken the book."),
                lambda: new_line()
            ],
            "inspect paper": [
                lambda: write("You pick up the paper, It's another note. It reads:"),
                lambda: new_line(),
                lambda: write("UGH, that warden thinks he is all high and mighty, swinging his keys around like he owns the place. I'll get him...He'll see...YES, AHAHA, I just need to get into that office of his!...of course I have to get him out first...", "dark cyan"),
                lambda: new_line(),
                lambda: write("    -Shadow", "dark cyan"),
                lambda: new_line(),
                lambda: pickup("note-2"),
                lambda: set_state("paper taken", True),
                lambda: set_state("book taken", False)
            ],
            "take paper": [
                lambda: write("You pick up the paper, It's another note. It reads:"),
                lambda: new_line(),
                lambda: write("UGH, that warden thinks he is all high and mighty, swinging his keys around like he owns the place. I'll get him...He'll see...YES, AHAHA, I just need to get into that office of his!...of course I have to get him out first...", "dark cyan"),
                lambda: new_line(),
                lambda: write("    -Shadow", "dark cyan"),
                lambda: new_line(),
                lambda: pickup("note-2"),
                lambda: set_state("paper taken", True),
                lambda: set_state("book taken", False)

            ],
        }
    ]
}


def set_state(name, value):
    states[name][0] = value


commands = { #The initial commands available in the room.
    "inspect room": [
        lambda: write("Straight ahead you can see a guard who is sitting at a desk listening to an antique radio whilst playing solitaire. Cells line the walls either side of you, some with inmates and some empty."),
        lambda: new_line()
    ],
    "inspect table": [
        lambda: write("The guard is sitting at the desk. On the desk is an antique radio playing some music."),
        lambda: new_line()
    ],
    "inspect book": [
        lambda: write("You open up the book and a piece of paper falls out."),
        lambda: new_line(),
        lambda: set_state("book taken", True)
    ],
    "inspect inmates": [
        lambda: write("You go close to an inmate's cell. He stares at you. All of a sudden his arm is stretched out trying to grab you. You jump back just in time! Phew!, I won't be doing that again."),
        lambda: new_line()
    ],
    "inspect radio": [
        lambda: write("I should probably leave that alone."),
        lambda: new_line()
    ],
    "inspect guard": [
        lambda: write("The guard is huge, seriously.. You don't wanna mess with him."),
        lambda: new_line()
    ],
    "inspect floor": [
        lambda: write("The floor is fitted stone and bricks. You notice a book on the floor in one of the empty cells, just in arm's reach."),
        lambda: new_line()
    ],
    "inspect cells": [
        lambda: write("Most of the inmates seem unstable, better not approach them. You notice a book on the floor in one of the empty cells, just in arm's reach."),
        lambda: new_line()
    ],
    "inspect ceiling": [
        lambda: write("The ceiling has a single light bulb per row, which illuminates the cells in pairs."),
        lambda: new_line()
    ],
    "inspect bulb": [
        lambda: write("Stop looking at the bulb, you'll hurt your eyes!"),
        lambda: new_line()
    ],
    "take book": [
        lambda: write("You open up the book and a piece of paper falls out."),
        lambda: new_line(),
        lambda: set_state("book taken", True)
    ],
    "go inmates": [
        lambda: write("You go close to an inmate's cell. He stares at you. All of a sudden his arm is stretched out trying to grab you. You jump back just in time! Phew!, I won't be doing that again."),
        lambda: new_line()
    ],
    "go door": [
        lambda: write("You walk back through the green doors into the shower room."),
        lambda: new_line(),
        lambda: change_room("shower room")
    ],
    #GO TO 2nd_corridor
    "go guard": [
        lambda: command_parser.game_over("The guard spots you immediately.") if not ("uniform(wearing)" in inventory) else None,
        lambda: write("You manage to walk past the guard without him even noticing!"),
        lambda: new_line(),
        lambda: change_room("second corridor")
    ]
}
