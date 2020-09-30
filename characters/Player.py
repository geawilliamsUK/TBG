class Player():
    def __init__(self,name):
        self.ycord = 50
        self.xcord = 50
        self.name = name
        self.health = 100
        self.armor = 0
        self.strength = 1

    def damage(self,hp):
        self.health -= hp
    def heal(self,hp):
        self.health +=hp
    def move(self,direction):#player can walk north, south, east, west
        if direction == "N":
            self.xcord -=1
        elif direction == "S":
            self.xcord +=1
        elif direction == "E":
            self.ycord -= 1
        elif direction == "W":
            self.ycord +=1
        print("player has moved, new cords Y: " + str(self.ycord) + " X: "+ str(self.xcord))

