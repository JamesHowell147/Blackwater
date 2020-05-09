#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from output import write, new_line

inventory = []


item_list = {
    "note": ["note1", "note-1"],
    "note-2": ["note2", "paper"],
    "note-3": ["note3"],
    "uniform(wearing)": ["clothes", "clothing", "outfit"],
    "uniform": ["clothes", "clothing", "outfit"],
    "xlax": [],
    "kcl": [],
    "narcozep": [],
    "meal": ["food"],
    "xlax-meal": ["meal", "food"],
    "kcl-meal": ["meal", "food"],
    "narcozep-meal": ["meal", "food"],
    "keys": ["keyring", "key"]
}


item_commands = {
    "note": {
        "inspect note": [
            lambda: write("The note reads:"),
            lambda: new_line(),
            lambda: write("I cannot take another day in this box, I WILL find a way out. And if not...  I'll have to make my own path to the outside. Every night where I sleep, I am one step closer, one hand full of dirt away from FREEDOM.", "dark cyan"),
            lambda: new_line(),
            lambda: write("    -Shadow", "dark cyan"),
            lambda: new_line()
        ]
    },
    "note-2": {
        "inspect note-2": [
            lambda: write("The note reads:"),
            lambda: new_line(),
            lambda: write("UGH, that warden thinks he is all high and mighty, swinging his keys around like he owns the place. I'll get him...He'll see...YES, AHAHA, I just need to get into that office of his!...of course I have to get him out first...", "dark cyan"),
            lambda: new_line(),
            lambda: write("    -Shadow", "dark cyan"),
            lambda: new_line()
        ]
    },
    "note-3": {
        "inspect note-3": [
            lambda: write("The note reads:"),
            lambda: new_line(),
            lambda: write("Hmmm, so close... and yet... so UNBEARABLY far. If only I could've gotten those keys! I'm afraid this might be the end...another failure... do you hear them? They must have noticed I was missing... at least they don't know about my plan, my messages!... next time I'll have everything I need!... Next time we can be free!", "dark cyan"),
            lambda: new_line(),
            lambda: write("    -Shadow", "dark cyan"),
            lambda: new_line()
        ]
    },
    "uniform": {
        "inspect uniform": [
            lambda: write("It's a chef's uniform."),
            lambda: new_line()
        ],
        "wear uniform": [
            lambda: write("You slip on the uniform over your overalls."),
            lambda: new_line(),
            lambda: drop("uniform"),
            lambda: pickup("uniform(wearing)")
        ],
    },
    "uniform(wearing)": {
        "inspect uniform(wearing)": [
            lambda: write("You're wearing a chef's uniform."),
            lambda: new_line()
        ]
    },
    "xlax": {
        "consume xlax": [
            lambda: command_parser.game_over("You immediately regret your decision as you sprint to the toilets. A guard notices you on the way.")
        ]
    },
    "kcl": {
        "consume kcl": [
            lambda: command_parser.game_over("You immediately drop dead.")

        ]
    },
    "narcozep": {
        "consume narcozep": [
            lambda: command_parser.game_over("You fall asleep on the spot. You wake up back in your cell.")

        ]
    },
    "meal": {
        "consume meal": [
            lambda: write("You probably shouldn't do that!."),
            lambda: new_line()
        ],
        "put kcl meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line(),
            lambda: drop("meal"),
            lambda: pickup("kcl-meal"),
            lambda: navigation.rooms["second corridor"].set_state("meal", False),
            lambda: navigation.rooms["second corridor"].set_state("kcl-meal", True)
        ],
        "put narcozep meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line(),
            lambda: drop("meal"),
            lambda: pickup("narcozep-meal"),
            lambda: navigation.rooms["second corridor"].set_state("meal", False),
            lambda: navigation.rooms["second corridor"].set_state("narcozep-meal", True)
        ],
        "put xlax meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line(),
            lambda: drop("meal"),
            lambda: pickup("xlax-meal"),
            lambda: navigation.rooms["second corridor"].set_state("meal", False),
            lambda: navigation.rooms["second corridor"].set_state("xlax-meal", True)
        ]
    },
    "kcl-meal": {
        "consume kcl-meal": [
            lambda: write("You probably shouldn't do that!."),
            lambda: new_line()
        ],
        "put kcl kcl-meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line()
        ],
        "put narcozep kcl-meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line()
        ],
        "put xlax kcl-meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line()
        ]
    },
    "narcozep-meal": {
        "consume narcozep-meal": [
            lambda: write("You probably shouldn't do that!."),
            lambda: new_line()
        ],
        "put kcl narcozep-meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line(),
            lambda: drop("narcozep-meal"),
            lambda: pickup("kcl-meal"),
            lambda: navigation.rooms["second corridor"].set_state("narcozep-meal", False),
            lambda: navigation.rooms["second corridor"].set_state("kcl-meal", True)
        ],
        "put narcozep narcozep-meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line()
        ],
        "put xlax narcozep-meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line(),
        ]
    },
    "xlax-meal": {
        "consume xlax-meal": [
            lambda: write("You probably shouldn't do that!."),
            lambda: new_line()
        ],
        "put kcl xlax-meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line(),
            lambda: drop("xlax-meal"),
            lambda: pickup("kcl-meal"),
            lambda: navigation.rooms["second corridor"].set_state("xlax-meal", False),
            lambda: navigation.rooms["second corridor"].set_state("kcl-meal", True)
        ],
        "put narcozep xlax-meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line(),
            lambda: drop("xlax-meal"),
            lambda: pickup("narcozep-meal"),lambda: navigation.rooms["second corridor"].set_state("xlax-meal", False),
            lambda: navigation.rooms["second corridor"].set_state("narcozep-meal", True)
        ],
        "put xlax xlax-meal": [
            lambda: write("You pour some of the bottle into the meal."),
            lambda: new_line()
        ]
    },
    "keys": {
    }
}


def pickup(name):
    if name in item_list:
        inventory.append(name)


def drop(name):
    if name in inventory:
        inventory.remove(name)


def print_inventory():
    if len(inventory) == 0:
        write("No items in inventory!", "red")
        new_line()
        return
    write("Inventory:", "magenta")
    for item in inventory:
        new_line()
        write(" ■ " + item.title(), "dark magenta")
    new_line()
