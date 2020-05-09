#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from output import write, new_line
from items import pickup, drop, inventory
import command_parser

name = "second corridor"

first_description = "You go around the corner and the corridor continues. There are a few doors you could take."
#Description given when you first enter the room.

previously_entered = False  #Keeps track of if the player has entered the room previously.

objects = {  #Every possible object in the room and synonyms.
    "walls": ["wall"],
    "floor": ["ground", "flooring"],
    "ceiling": ["roof"],
    "room": ["around", "corridor"],
    "office": [],
    "infirmary": ["hospital", "ward", "doctors", "doctor's", "medic", "med", "medical"],
    "atrium": ["hall", "end"],
    "stairwell": ["stairs", "stair"]
}

states = {  #Used to add or overwrite commands when the state of the room changes.
    "taken bottle": [
        False, {
            "inspect room": [
                lambda: write("The Warden's door is just ahead of you.") if states["meal"][0] or states["xlax-meal"][0] or states["narcozep-meal"][0] or states["kcl-meal"][0] else write("You can go down the corridor into the Atrium, back into the infirmary, or you can try the Warden's door."),
                lambda: change_room(warden_office.py),
                lambda: new_line()
            ]
        }
    ],
    "meal": [
        False, {
            "go office": [
                lambda: write("You knock at the Warden's door. after a few seconds of footsteps, the Warden opens the door."),
                lambda: new_line(),
                lambda: write("'Thank you. I'm absolutely starving.'", "dark green"),
                lambda: new_line(),
                lambda: write("He takes the tray of food from your hands, walks back to his desk and sits back in his chair before shoving a large spoon-full of food into his mouth."),
                lambda: new_line(),
                lambda: write("He glances up at you."),
                lambda: new_line(),
                lambda: write("'You may go.'", "dark green"),
                lambda: new_line(),
                lambda: write("He says, dismissing you. You walk back out into the corridor, you came so close. Suddenly, a naked man escourted be the guard from earlier comes around the corner."),
                lambda: new_line(),
                lambda: write("'There he is!'", "dark green"),
                lambda: new_line(),
                lambda: write("'There he is!'", "dark green"),
                lambda: new_line("Yells the naked man."),
                lambda: command_parser.game_over("Looks like you're out of luck...")
            ]
        }
    ],
    "xlax-meal": [
        False, {
            "go office": [
                lambda: write("You knock at the Warden's door. after a few seconds of footsteps, the Warden opens the door."),
                lambda: new_line(),
                lambda: write("'Thank you. I'm absolutely starving.'", "dark green"),
                lambda: new_line(),
                lambda: write("He takes the tray of food from your hands, walks back to his desk and sits back in his chair before shoving a large spoon-full of food into his mouth."),
                lambda: new_line(),
                lambda: write("He glances up at you."),
                lambda: new_line(),
                lambda: write("'Y...'", "dark green"),
                lambda: new_line(),
                lambda: write("He pauses, before jumping up out of his chair and sprinting down the corridor, towards the toilets."),
                lambda: new_line(),
                lambda: write("You hesitate for a moment before stepping into the room."),
                lambda: new_line(),
                lambda: set_state("xlax-meal", False),
                lambda: set_state("meal eaten", True),
                lambda: change_room("warden's office")
            ]
        }
    ],
    "narcozep-meal": [
        False, {
            "go office": [
                lambda: write("You knock at the Warden's door. after a few seconds of footsteps, the Warden opens the door."),
                lambda: new_line(),
                lambda: write("'Thank you. I'm absolutely starving.'", "dark green"),
                lambda: new_line(),
                lambda: write("He takes the tray of food from your hands, walks back to his desk and sits back in his chair before shoving a large spoon-full of food into his mouth."),
                lambda: new_line(),
                lambda: write("He glances up at you."),
                lambda: new_line(),
                lambda: write("'Y...'", "dark green"),
                lambda: new_line(),
                lambda: write("He trails off and falls gently back into his chair."),
                lambda: new_line(),
                lambda: write("You hesitate for a moment before stepping into the room."),
                lambda: new_line(),
                lambda: set_state("narcozep-meal", False),
                lambda: set_state("meal eaten", True),
                lambda: rooms["warden's office"].set_state("warden asleep", True),
                lambda: change_room("warden's office")
            ]
        }
    ],
    "kcl-meal": [
        False, {
            "go office": [
                lambda: write("You knock at the Warden's door. after a few seconds of footsteps, the Warden opens the door."),
                lambda: new_line(),
                lambda: write("'Thank you. I'm absolutely starving.'", "dark green"),
                lambda: new_line(),
                lambda: write("He takes the tray of food from your hands, walks back to his desk and sits back in his chair before shoving a large spoon-full of food into his mouth."),
                lambda: new_line(),
                lambda: write("He glances up at you."),
                lambda: new_line(),
                lambda: write("'Y...'", "dark green"),
                lambda: new_line(),
                lambda: write("He cuts off, falling back suddenly into his chair. He is completely still."),
                lambda: new_line(),
                lambda: write("You hesitate for a moment before stepping into the room."),
                lambda: new_line(),
                lambda: set_state("kcl-meal", False),
                lambda: set_state("meal eaten", True),
                lambda: rooms["warden's office"].set_state("warden dead", True),
                lambda: change_room("warden's office")
            ]
        }
    ],
    "lever pulled": [
        False, {
            "look room": [
                lambda: write("Further up the corridor, you see utter chaos...what looks like every guard in the facility trying desperately to control the inmates you set free. Down the corridor is an empty Atrium."),
                lambda: new_line()
            ],
            "go stairwell": [
                lambda: write("The gate to the stairwell is situated in the middle of the action, it's probably best if you don't go there."),
                lambda: new_line()
            ],
            "go atrium": [
                lambda: write("You walk back down into the Atrium."),
                lambda: new_line(),
                lambda: change_room("atrium")
            ]
        }
    ],
    "meal eaten": [
        False, {
            "go office": [
                lambda: write("You step pack into the office."),
                lambda: new_line(),
                lambda: change_room("warden's office")
            ]
        }
    ]
}


def set_state(name, value):
    states[name][0] = value


commands = {  #The initial commands available in the room.
    "inspect room": [
        lambda: write("You are back in the corridor, the Infirmary door is still unlocked.") if states["meal"][0] or states["xlax-meal"][0] or states["narcozep-meal"][0] or states["kcl-meal"][0] else write("You're in a rather derelict looking corridor. There is a locked gate on the corner marked 'stairwell'. Down the corridor you see doors to the Warden's Office and the Infirmary. The end of the corridor opens out into the Atrium."),
        lambda: new_line()
    ],
    "inspect walls": [
        lambda: write("The walls are old and cracked, and are barely holding together, but are stable enough to just keep the corridoor standing."),
        lambda: new_line()
    ],
    "inspect floor": [
        lambda: write("The floor is made up of rough flagstone tiles, which appear to be very old, they are dirty and are weathered."),
        lambda: new_line()
    ],
    "inspect ceiling": [
        lambda: write("The ceiling is supported by rusted steel beams along with metal pipes, from which there is continuous water dripping."),
        lambda: new_line()
    ],
    "inspect office": [
        lambda: write("The door to the Warden's Office is solid, no windows."),
        lambda: new_line()
    ],
    "inspect infirmary": [
        lambda: write("There is a note stuck to the door that says:"),
        lambda: new_line(),
        lambda: write("Out for lunch.", "dark cyan"),
        lambda: new_line(),
        lambda: write("Dispite this, the doors have been left unlocked."),
        lambda: new_line()
    ],
    "inspect atrium": [
        lambda: write("The end of the corridor leads out into the Atrium, the central room in the facility."),
        lambda: new_line()
    ],
    "inspect stairwell": [
        lambda: write("The stairwell leads upto the other cells. The enterance is gated shut."),
        lambda: new_line()
    ],
    "go office": [
        lambda: write("You walk up to the warden's office and try the door, but it's locked."),
        lambda: new_line()
    ],
    "go stairwell": [
        lambda: write("You walk up to the stairwell gate and try opening it. It doesn't budge."),
        lambda: new_line(),
        lambda: write("Whoa, déjà vu...never mind..."),
        lambda: new_line()
    ],
    "go infirmary": [
        lambda: write("You walk down towards the infirmary. The door is left open. You check the area around you to make sure no one is nearby before slipping between the double doors. "),
        lambda: change_room("infirmary"),
        lambda: new_line()
    ],
    "go atrium": [
        lambda: write("You continue along the old corridor into the Atrium."),
        lambda: new_line(),
        lambda: change_room("atrium")
    ],
    "go back": [
        lambda: change_room(get_last_room()) if get_last_room() != "cell corridor" else write("You probably shouldn't try your luck again with the guard."),
        lambda: new_line()
    ]
}
