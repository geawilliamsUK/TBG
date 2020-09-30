from libs.characters.Player import Player
from libs.Map.Map import Map
from libs.Commands.Commands import movement_commands


world = Map()
name = input("enter your characters name: ")
MC = Player(name,world)
playing = True
while playing == True:
    command = input("what would you like to do? ")



