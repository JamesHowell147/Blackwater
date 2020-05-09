#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from output import write, new_line
from items import pickup, drop

name = "warden's office"

first_description = "You tread carefully as if you'd just entered a dragon's lair." #Description given when you first enter the room.

previously_entered = False  #Keeps track of if the player has entered the room previously.

objects = {  #Every possible object in the room and synonyms.
    "walls": ["wall"],
    "desk": ["bench", "worktop", "table", "bar", "workbench", "worktable"],
    "door": ["entrance", "doorway", "exit", "back", "leave", "out", "corridor", "doors"],
    "keys": ["key", "keyring"],
    "chair": ["seat"],
    "floor": ["ground", "flooring", "carpet"],
    "ceiling": ["roof"],
    "clock": ["time"],
    "room": ["around"],
    "file": ["folder"],
    "note": ["paper"],
    "drawer": ["draw"],
    "lever": ["switch"]
}

states = { #Used to add or overwrite commands when the state of the room changes.
    "file found": [
        False, {
            "inspect file": [
                lambda: write("Hmm... Numerous escape attempts, very unstable, refers to themselves, only as 'Shadow', do not attempt conversation. Prone to...memory loss..."),
                lambda: new_line(),
                lambda: write("Your eyes whip to the image at the top of the document, you immediately recognise the face... confirming what you feared..."),
                lambda: new_line(),
                lambda: write("..."),
                lambda: new_line(),
                lambda: pickup("file"),
                lambda: write("A final note falls from the file. It reads:"),
                lambda: new_line(),
                lambda: write("Hmmm, so close... and yet... so UNBEARABLY far. If only I could've gotten those keys! I'm afraid this might be the end...another failure... do you hear them? They must have noticed I was missing... at least they don't know about my plan, my messages!... next time I'll have everything I need!... Next time we can be free!", "dark cyan"),
                lambda: new_line(),
                lambda: write("    -Shadow", "dark cyan"),
                lambda: new_line(),
                lambda:pickup("note-3")
            ],
            "take file": [
                lambda: write("Hmm... Numerous escape attempts, very unstable, do not attempt conversation. Prone to...memory loss..."),
                lambda: new_line(),
                lambda: write("Your eyes whip to the image at the top of the document, you immediately recognise the face... confirming what you feared..."),
                lambda: new_line(),
                lambda: write("..."),
                lambda: new_line(),
                lambda: pickup("file"),
                lambda: write("A final note falls from the file. It reads:"),
                lambda: new_line(),
                lambda: write("Hmmm, so close... and yet... so UNBEARABLY far. If only I could've gotten those keys! I'm afraid this might be the end...another failure... do you hear them? They must have noticed I was missing... at least they don't know about my plan, my messages!... next time I'll have everything I need!... Next time we can be free!", "dark cyan"),
                lambda: new_line(),
                lambda: write("    -Shadow", "dark cyan"),
                lambda: new_line(),
                lambda:pickup("note-3")
            ],
        }
    ],
    "warden dead": [
        False, {
            "inspect room": [
                lambda: write("There's a large desk in the middle of the room with a few drawers and a chair. The warden's body is lies still in the chair, you notice a large bunch of keys hanging from his pocket.  On the wall you see a large lever."),
                lambda: new_line()
            ],
            "inspect chair": [
                lambda: write("It's just an ordinary office chair. In it lies the warden."),
                lambda: new_line()
            ],
            "inspect warden": [
                lambda: write("The warden is lying perfectly still in the chair, all life has left his body. In his pocket, you notice a large ring of keys."),
                lambda: new_line()
            ],
            "take keys": [
                lambda: write("You grab the bunch of keys from the pocket of the sleeping warden.") if not states["keys taken"][0] else write("You've already picked up the keys."),
                lambda: new_line(),
                lambda: pickup("keys") if not states["keys taken"][0] else None,
                lambda: set_state("keys taken", True)
            ]
        }
    ],
    "warden asleep": [
        False, {
            "inspect room": [
                lambda: write("There's a large desk in the middle of the room with a few drawers and a chair. The warden's is lying in the chair, snoring loudly. You notice a large bunch of keys hanging from his pocket.  On the wall you see a large lever."),
                lambda: new_line()
            ],
            "inspect chair": [
                lambda: write("It's just an ordinary office chair. In it lies the warden."),
                lambda: new_line()
            ],
            "inspect warden": [
                lambda: write("The warden is lying in the chair fast asleep, snoring heavily. In his pocket, you notice a large ring of keys."),
                lambda: new_line()
            ],
            "take keys": [
                lambda: write("You grab the bunch of keys from the pocket of the sleeping warden.") if not states["keys taken"][0] else write("You've already picked up the keys."),
                lambda: new_line(),
                lambda: pickup("keys") if not states["keys taken"][0] else None,
                lambda: set_state("keys taken", True)
            ]
        }
    ],
    "file read": [
        False, {
            "move drawer": [
                lambda: write("There's nothing else of interest in the drawers."),
                lambda: new_line()
            ],
            "inspect drawer": [
                lambda: write("There's nothing else of interest in the drawers."),
                lambda: new_line()
            ]
        }
    ],
    "keys taken": [
        False, {
            "take keys": [
                lambda: write("You've already picked up the keys."),
                lambda: new_line()
            ]
        }
    ],
    "lever pulled": [
        False, {
            "move lever": [
                lambda: write("You try to push the leaver back up but it won't budge."),
                lambda: new_line()
            ]
        }
    ],
}


def set_state(name, value):
    states[name][0] = value


commands = { #The initial commands available in the room.
    "inspect room": [
        lambda: write("There's a large desk in the middle of the room with a few drawers and a chair. On the wall you see a large lever."),
        lambda: new_line()
    ],
    "inspect desk": [
        lambda: write("The desk is large and very tidy, atop sits a small clock. It also has a few drawers on either side."),
        lambda: new_line()
    ],
    "inspect chair": [
        lambda: write("In the chair, you see a large bunch of keys. The warden must have left them behind in his panic."),
        lambda: new_line()
    ],
    "inspect door": [
        lambda: write("The door leads back into the corridor."),
        lambda: new_line()
    ],
    "inspect drawer": [
        lambda: write("Most of the draws contain contain nothing of interest. You find one which seems to enclose files on all of the prisoners, as you scan over them, your eyes are drawn to a familiar name, 'Shadow'."),
        lambda: new_line(),
        lambda: set_state("file found", True)
    ],
    "inspect wall": [
        lambda: write("The walls are painted a kind of off white. On one wall is a large lever."),
        lambda: new_line()
    ],
    "inspect lever": [
        lambda: write("The leaver is labled 'Emergency Door Release'."),
        lambda: new_line()
    ],
    "inspect floor": [
        lambda: write("The floor is layed with deep blue carpet. It's very comfortable to walk on."),
        lambda: new_line()
    ],
    "inspect ceiling": [
        lambda: write("The ceiling is painted white and is a little lower than some of the other rooms."),
        lambda: new_line()
    ],
    "inspect keys": [
        lambda: write("There are about twenty keys on a large metal ring, you wonder what they they could all used for."),
        lambda: new_line()
    ],
    "inspect clock": [
        lambda: write("The time is 13:07, just after lunch time."),
        lambda: new_line()
    ],
    "go door": [
        lambda: write("You exit the room, back into the corridor."),
        lambda: new_line(),
        lambda: change_room("second corridor")
    ],
    "move drawer": [
        lambda: write("Most of the draws contain nothing of interest. You find one however which seems to enclose files on all of the prisoners, as you scan over them, your eyes are drawn to a familiar name, 'Shadow'."),
        lambda: new_line(),
        lambda: set_state("file found", True)
    ],
    "move lever": [
        lambda: write("You pull on the lever and a siren immediately sounds. You hear rushing footsteps from every direction as guards charge to deal with the other inmates."),
        lambda: new_line(),
        lambda: write("The noise of feet rushing by the door is quickly replaced by that of rowdy inmates as they guards arrive at the scene. You don't hear any noise from the direction of the main atrium."),
        lambda: set_state("lever pulled", True),
        lambda: rooms["second corridor"].set_state("lever pulled", True),
        lambda: rooms["atrium"].set_state("lever pulled", True)
    ],
    "take keys": [
        lambda: write("You pick up the keys from the chair and deposit them into your pocket."),
        lambda: new_line(),
        lambda: pickup("keys"),
        lambda: set_state("keys taken", True)
    ]
}
