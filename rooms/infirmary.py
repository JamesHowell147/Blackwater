#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from output import write, new_line
from items import pickup, drop

name = "infirmary"

first_description = "You walk into the infirmary, while keeping an eye on the warden's office  across the hall."  #Description given when you first enter the room.

previously_entered = False #Keeps track of if the player has entered the room previously.

objects = { #Every possible object in the room and synonyms.
    "walls": ["wall"],
    "table": ["bench", "worktop", "desk", "bar", "workbench", "worktable"],
    "door": ["entrance", "doorway", "hatch", "exit", "back", "corridor", "out", "doors"],
    "floor": ["ground", "flooring"],
    "ceiling": ["roof"],
    "room": ["around"],
    "case": ["glass"],
    "cabinet": ["cupboard"],
    "xlax": [],
    "kcl": [],
    "narcozep": []

}

states = { #Used to add or overwrite commands when the state of the room changes.
    
}


def set_state(name, value):
    states[name][0] = value


commands = { #The initial commands available in the room.
    "inspect room": [
        lambda: write("It's a large shiny room with high top chairs, surgery tables and  cabinets all around. There is spotless medical equipment locked behind glass cases. A few cabinets are left open."),
        lambda: new_line()
    ],
    "inspect table": [
        lambda: write("The table holds medical books. After flicking through a few pages, you  remember why you didn't pick medicine."),
        lambda: new_line()
    ],
    "inspect case": [
        lambda: write("The glass case is locked shut."),
        lambda: new_line()
    ],
    "inspect cabinet": [
        lambda: write("You rummage through the cabinet, you find a few strangely labelled bottles  including: XLAX, KCL, and Narcozep."),
        lambda: new_line()
    ],
    "move cabinet": [
        lambda: write("You rummage through the cabinet, you find a few strangely labelled bottles  including: XLAX, KCL, and Narcozep."),
        lambda: new_line()
    ],
    "take xlax": [
        lambda: write("You pick up the XLAX bottle and put it in your pocket."),
        lambda: pickup("xlax"),
        lambda: new_line()
    ],
    "take kcl": [
        lambda: write("You pick up the KCL bottle and put it in your pocket."),
        lambda: pickup("kcl"),
        lambda: new_line()
    ],
    "take narcozep": [
        lambda: write("You pick up the Narcozep bottle and put it in your pocket"),
        lambda: pickup("narcozep"),
        lambda: new_line()
    ],
    "go door": [
        lambda: write("You quickly scurry out of the infirmary and back into the corridor."),
        lambda: new_line(),
        lambda: change_room("second corridor")
    ]
}
