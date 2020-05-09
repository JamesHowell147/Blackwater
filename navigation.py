#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import rooms.starting_cell
import rooms.shower_room
import rooms.cell_corridor
import rooms.second_corridor
import rooms.wardens_office
import rooms.infirmary
import rooms.atrium
import sys
from output import write, new_line

# sys.modules is a dictionary of all modules which have been imported
# during the current session. Since the module had to be imported to
# access it, it will be in there. '__name__' is available inside functions because it is in the module scope.
this = sys.modules[__name__]

current_room = None

last_room = ""

rooms = {
    "starting cell": rooms.starting_cell,
    "shower room": rooms.shower_room,
    "cell corridor": rooms.cell_corridor,
    "second corridor": rooms.second_corridor,
    "warden's office": rooms.wardens_office,
    "infirmary": rooms.infirmary,
    "atrium": rooms.atrium
}


def change_room(room):
    global current_room
    global last_room
    last_room = current_room
    current_room = rooms[room]
    if not current_room.previously_entered:
        write(current_room.first_description)
        new_line()
        current_room.previously_entered = True
    write(room.title() + ":", "magenta")
    new_line()


def get_last_room():
    return last_room.name



for room in rooms:
    rooms[room].change_room = this.change_room
    rooms[room].get_last_room = this.get_last_room
    rooms[room].rooms = this.rooms

change_room("starting cell")
