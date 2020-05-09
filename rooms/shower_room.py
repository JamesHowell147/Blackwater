#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from output import write, new_line
from items import pickup, drop

name = "shower room"

first_description = "You drop down into the shower room"
#Description given when you first enter the room.
previously_entered = False #Keeps track of if the player has entered the room previously.

objects = { #Every possible object in the room and synonyms.
    "walls": ["wall"],
    "door": ["entrance", "doorway", "doors", "exit", "out"],
    "window": ["opening", "bars", "hatch"],
    "floor": ["ground", "flooring"],
    "ceiling": ["roof"],
    "shower": ["drain", "cubicle", "showers", "drains", "cubicles"],
    "lockers": ["cabinet"],
    "uniform": ["clothes", "clothing", "outfit"],
    "room": ["around"],
    "door": ["entrance", "doorway", "exit", "leave", "corridor", "corridors", "out", "doors"],
    "hole": ["grate", "grill", "vent", "ventilation"],
    "bench": ["seat"],
    "back": []
}

states = { #Used to add or overwrite commands when the state of the room changes.
    "clothes taken": [
        False, {
            "take uniform": [
                lambda: write("You've already taken the clothes."),
            ]
        }
    ]

}


def set_state(name, value):
    states[name][0] = value


commands = { #The initial commands available in the room.
    "inspect room": [
        lambda: write("You look around the room. There is cold textured stone covering the floor, walls and ceiling. You are in one of six shower cubicles in a line to your right with small changing benches and lockers to your left. There is someone taking a shower with their clothes left on a bench. There is a bright green door leading to the corridor next to the changing rooms."),
        lambda: new_line()
    ],
    "inspect door": [
        lambda: write("The large green double doors are is unlocked."),
        lambda: new_line()
    ],
    "inspect window": [
        lambda: write("The windows are fitted with iron bars."),
        lambda: new_line()
    ],
    "inspect wall": [
        lambda: write("The cold walls are solid, nothing of interest."),
        lambda: new_line()
    ],
    "inspect floor": [
        lambda: write("The cold floor is solid, yet slippery, nothing of interest."),
        lambda: new_line()
    ],
    "inspect ceiling": [
        lambda: write("You can't reach the ceiling, there are dozens of light bulbs swinging illuminating the room."),
        lambda: new_line()
    ],
    "inspect uniform": [
        lambda: write("There are chef clothes along with a chef's hat and apron."),
        lambda: new_line()
    ],
    "inspect lockers": [
        lambda: write("Some of the lockers are locked, the others are all empty."),
        lambda: new_line()
    ],
    "inspect bench": [
        lambda: write("Somebody's left their clothes out on the bench."),
        lambda: new_line()
    ],
    "inspect shower": [
        lambda: write("You can hear somebody in one of the showers, the clothes must belong to them."),
        lambda: new_line()
    ],
    "take uniform": [
        lambda: write("You take the clothes."),
        lambda: new_line(),
        lambda: pickup("uniform"),
        lambda: set_state("clothes taken", True)
    ],
    "go door": [
        lambda: write("You open the door and walk through."),
        lambda: new_line(),
        lambda: change_room("cell corridor")
    ],
    "go shower": [
        lambda: write("You don't have time for a shower!"),
        lambda: new_line()
    ],
    "go hole": [
        lambda: write("You try to jump up but you can't reach."),
        lambda: new_line()
    ],
    "go back": [
        lambda: change_room("cell corridor") if get_last_room() == "cell corridor" else write("You try to jump up but you can't reach."),
        lambda: new_line()
    ]
}
