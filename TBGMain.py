from characters.Player import Player

name = input("enter your characters name: ")
MC = Player(name)
playing = True
while playing == True:
    command = input("what would you like to do? ")
    if command == "walk north":
        MC.move("N")
    if command == "walk south":
        MC.move("S")
    if command == "walk east":
        MC.move("E")
    if command == "walk west":
        MC.move("W")