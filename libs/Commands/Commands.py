def movement_commands(command, world, player):
    if command == "walk north":
        player.move("N", world)
    if command == "walk south":
        player.move("S", world)
    if command == "walk east":
        player.move("E", world)
    if command == "walk west":
        player.move("W", world)