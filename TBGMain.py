from characters.Player import Player
from Map.Map import Map
world = Map()
name = input("enter your characters name: ")
MC = Player(name,world)
playing = True
while playing == True:
    command = input("what would you like to do? ")
    if command == "walk north":
        MC.move("N", world)
    if command == "walk south":
        MC.move("S", world)
    if command == "walk east":
        MC.move("E", world)
    if command == "walk west":
        MC.move("W", world)
    if command == "show map":
        showMap(world)


