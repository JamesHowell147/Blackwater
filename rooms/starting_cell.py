#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from output import write, new_line
from items import pickup, drop

name = "starting cell"

first_description = "You wake up to the distant clanking of metal in otherwise dead silence..."  #Description given when you first enter the room.

previously_entered = False  #Keeps track of if the player has entered the room previously.

objects = {  #Every possible object in the room and synonyms.
    "walls": ["wall"],
    "table": ["bench", "worktop", "desk", "bar", "workbench", "worktable"],
    "door": ["entrance", "doorway", "hatch", "exit", "doors"],
    "window": ["opening", "bars", "hatch"],
    "floor": ["ground", "flooring"],
    "walls": ["wall"],
    "ceiling": ["roof"],
    "mattress": ["bed", "cussion", "futon"],
    "room": ["around"],
    "note": ["paper", "message"],
    "grill": ["grate", "gate"],
    "flagstones": ["tiles", "stones", "tile", "flagstone", "stone"],
    "tunnel": ["hole"],
    "crack": ["fissure", "cracks"]
}

states = {  #Used to add or overwrite commands when the state of the room changes.
    "note read": [
        False, {
            "inspect mattress": [
                lambda: write("The mattress looks quite old and ragged."),  #lambdas are 1 line functions.
                lambda: new_line()
            ],
            "move mattress": [
                lambda: write("You shift the mattress a few inches accross the floor."),
                lambda: new_line()
            ],
            "inspect floor": [
                lambda: write("The crack originates at a large patch of loose, cracked flagstones previously covered by the mattress."),
                lambda: new_line()
            ],
            "inspect crack": [
                lambda: write("The crack originates at a large patch of loose, cracked flagstones previously covered by the mattress."),
                lambda: new_line()
            ],
            "inspect flagstones": [
                lambda: write("You crouch down and start to remove some of the pieces of the broken flagstone. To your amazement you reveal a small, dark tunnel that seems to be leading somewhere."),
                lambda: new_line(),
                lambda: set_state("tunnel uncovered", True)
            ],
            "move flagstones": [
                lambda: write("You crouch down and start to remove some of the pieces of the broken flagstone. To your amazement you reveal a small, dark tunnel that seems to be leading somewhere."),
                lambda: new_line(),
                lambda: set_state("tunnel uncovered", True)
            ]
        }
    ],
    "in tunnel": [
        False, {
            "go tunnel": [
                lambda: write("You're already in the tunnel"),
                lambda: new_line(),
            ],
            "move grill": [
                lambda: write("You carefully push open the grill, trying to stay quiet."),
                lambda: new_line(),
                lambda: change_room("shower room")
            ],
            "go back": [
                lambda: write("You can't get back up."),
                lambda: new_line(),
            ],
            "inspect room": [
                lambda: write("You can't see much from inside the tunnel."),
                lambda: new_line()
            ],
            "inspect table": [
                lambda: write("You can't see the table from here."),
                lambda: new_line()
            ],
            "inspect door": [
                lambda: write("You can't see the door from here."),
                lambda: new_line()
            ],
            "inspect window": [
                lambda: write("You can't see the window from here."),
                lambda: new_line()
            ],
            "inspect wall": [
                lambda: write("The walls of the tunnel are dirt."),
                lambda: new_line()
            ],
            "inspect floor": [
                lambda: write("The floor of the tunnel is dirt."),
                lambda: new_line()
            ],
            "inspect crack": [
                lambda: write("You can't see the crack from here."),
                lambda: new_line()
            ],
            "inspect ceiling": [
                lambda: write("The ceiling of the tunnel is dirt."),
                lambda: new_line()
            ],
            "inspect mattress": [
                lambda: write("You can't see the matttress from here."),
                lambda: new_line()
            ],
        }
    ],
    "tunnel uncovered": [
        False, {
            "go tunnel": [
                lambda: write("You slowly lower yourself into the tunnel, which seems to get smaller and more cramped as you move. After crawling for five or six metres, you are able to see where the tunnel meets the side of a ventilation shaft. You continue to crawl until you see that you are outside what seems to be the shower room, behind a loose mesh grill."),
                lambda: new_line(),
                lambda: set_state("in tunnel", True)
            ]
        }
    ]
}


def set_state(name, value):
    states[name][0] = value


commands = {  #The initial commands available in the room.
    "inspect room": [
        lambda: write("You're surrounded by rough stone walls on all sides, with a heavy iron door at the far end featuring a small barred window. The floor is made  up of large flagstones. There is a rugged mattress on the floor against the back  wall and a battered wooden desk in the centre of the room."),
        lambda: new_line()
    ],
    "inspect table": [
        lambda: write("The table stands in the centre of the room, its entire surface covered in  etchings of names and drawings from others like you. You wonder what  became of them, perhapse you might meet a similar fate."),
        lambda: new_line()
    ],
    "inspect door": [
        lambda: write("You try to push the solid iron door but it won't budge."),
        lambda: new_line()
    ],
    "inspect window": [
        lambda: write("The windows are too small to fit through, even if you managed to break the bars."),
        lambda: new_line()
    ],
    "inspect wall": [
        lambda: write("The white stone walls are cold, they draw heat and emotion from the room."),
        lambda: new_line()
    ],
    "inspect floor": [
        lambda: write("The floor is fitted with flagstones, a deep crack originates from under the mattress and runs across the room."),
        lambda: new_line()
    ],
    "inspect crack": [
        lambda: write("The crack seems to originate from under the mattress."),
        lambda: new_line()
    ],
    "inspect ceiling": [
        lambda: write("The ceiling in this room is made of brick, although it is covered in a mesh."),
        lambda: new_line()
    ],
    "inspect mattress": [
        lambda: write("The mattress lies with one edge against the back wall. A large crack originates from underneath."),
        lambda: new_line()
    ],
    "move mattress": [
        lambda: write("The mattress moves easily, revealing some loose, cracked flagstones. When you slide it to the side you notice a note that was stuffed underneath."),
        lambda: new_line(),
        lambda: write("The note reads:"),
        lambda: new_line(),
        lambda: write("I cannot take another day in this box, I WILL find a way out. And if not...  I'll have to make my own path to the outside. Every night where I sleep, I am one step closer, one hand full of dirt away from FREEDOM.", "dark cyan"),
        lambda: new_line(),
        lambda: write("    -Shadow", "dark cyan"),
        lambda: new_line(),
        lambda: set_state("note read", True),
        lambda: pickup("note"),
        lambda: new_line()
    ]
}
