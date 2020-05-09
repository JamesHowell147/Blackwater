#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from output import write, new_line
from items import pickup, drop, inventory

name = "atrium"

first_description = "You are now in the Atrium"

previously_entered = False #Keeps track of if the player has entered the room previously.

objects = { #Every possible object in the room and synonyms.
    "walls": ["wall"],
    "table": ["bench", "worktop", "desk", "bar", "workbench", "worktable","reception"],
    "door": ["entrance", "doorway", "hatch", "exit", "out", "doors"],
    "room": ["around"],
    "note": [],
    "cafeteria": ["kitchen", "dining", "lunch"],
    "corridor": ["back", "second_corridor", "hallway", "hall"]


}

states = { #Used to add or overwrite commands when the state of the room changes.
    "food taken": [
        False, {
            "go cafeteria": [
                lambda: write("You should probably deliver this food before you go back in there, if you don't want to get shouted at...") #lambdas are 1 line functions.
            ]
        }
    ],
    "lever pulled": [
        False, {
            "go cafeteria": [
                lambda: write("The cafeteria door has been locked shut."),
                lambda: write(" You try a few keys in the lock but it seems that the kitchen staff have barricaded themselves in.") if ("keys" in inventory) else None,
                lambda: new_line()
            ],
            "inspect cafeteria": [
                lambda: write("The doors to the cafeteria have been locked shut."),
                lambda: new_line()
            ],
            "inspect door": [
                lambda: write("The door is locked"),
                lambda: new_line()
            ],
            "go door": [
                lambda: win_game() if ("keys" in inventory) else write("The door is locked"),
                lambda: new_line()
            ],
            "move door": [
                lambda: win_game() if ("keys" in inventory) else write("The door is locked"),
                lambda: new_line()
            ],
            "put keys door": [
                lambda: win_game() if ("keys" in inventory) else write("You don't have the keys"),
                lambda: new_line()
            ],
            "move keys": [
                lambda: win_game() if ("keys" in inventory) else write("You don't have the keys"),
                lambda: new_line()
            ],
            "inspect room": [
                lambda: write("The Atrium is empty now. The door to the cafeteria has been locked shut. The main exit is still locked."),
                lambda: new_line()
            ]
        }
    ]
}


def set_state(name, value):
    states[name][0] = value


commands = { #The initial commands available in the room.
    "inspect room": [
        lambda: write("You are now in the Atrium. There is a group of guards having a discussion. You can see the main exit door and an open enterance into the cafeteria, where most of the staff are eating their lunch."),
        lambda: new_line()
    ],
    "inspect wall": [
        lambda: write(" Stone walls all around the building"),
        lambda: new_line()
    ],
    "inspect floor": [
        lambda: write("The floor has an unusual stone tile design"),
        lambda: new_line()
    ],
    "inspect door": [
        lambda: write("The door is bolted shut. The bolts are secured in place with padlocks."),
        lambda: new_line()
    ],
    "move door": [
        lambda: write("The door is bolted shut."),
        lambda: new_line()
    ],
    "go door": [
        lambda: write("The door is bolted shut."),
        lambda: new_line()
    ],
    "go corridor": [
        lambda: write("You walk back into the corridor"),
        lambda: new_line(),
        lambda: change_room("second corridor")
    ],
    "go cafeteria": [
        lambda: write("Cafeteria:", "magenta"),
        lambda: new_line(),
        lambda: write("You go through the doors and are immediately approached by a agitated looking member of the kitchen staff. Their face has a reddish hue."),
        lambda: new_line(),
        lambda: write("'YOU'RE LATE! Where have you been!? The Warden's been waiting for his food!'", "dark green"),
        lambda: new_line(),
        lambda: write("He hands you the Warden's meal."),
        lambda: new_line(),
        lambda: write("'Take it to his office, he should be in there!'", "dark green"),
        lambda: new_line(),
        lambda: write("He ushers you out of the doors, back into the Atrium."),
        lambda: new_line(),
        lambda: write("Atrium:", "magenta"),
        lambda: new_line(),
        lambda: pickup("meal"),
        lambda: set_state("food taken", True),
        lambda: rooms["second corridor"].set_state("meal", True)
    ]
}
