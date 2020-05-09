# Blackwater
A python **VERSION 2.7** based text adventure game. I designed and developed this game as part of a three person team for a final module project.

Game description

Run __main__.py in the modules folder.

In terms of the structure of the program,

There is the main loop which continuously takes the user input and parses it.

Each room also has a list of all of the referenceable objects in it.

There is a global list of recognised nouns.

All words come with lists of synonyms.

The text parser culls any words that are not in the room's object list, the verb list or the names of items in your inventory.

Each room has a list of commands and a list of toggleable states which can add or override commands.

Each item also has a list of associated commands.

The parser checks through the lists of commands and tries to find a match.

Each command has a list of lambda functions attached to it which are run in order if the command is matched to the input.

If there is no match, the parser tries to figure out what you were saying so it gan give a more relevant error.

It looks at whether the first word was a recognised verb and then if the subsequent words are recognised objects.

It tried to give the most relevant version of "You can't do that" that it can.

Everything really happens in the lambda functions attached to the commands. They check conditions, toggle the states in the rooms, move you between rooms, pick up and drop items, etc.

Finally all messages are printed through out output.py module. This allows us to apply an effect in which each character is printed in a sequence. We also ensure that no words go between 2 lines.
