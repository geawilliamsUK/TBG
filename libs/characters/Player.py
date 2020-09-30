class Player():
    def __init__(self,name,map):
        self.ycord = 50
        self.xcord = 50
        self.name = name
        self.health = 100
        self.armor = 0
        self.strength = 1

    def damage(self,e,world):
        self.health -= e.strength
        print("a goblin attacked you, you lost "+ str(e.strength) + " health")
        print("your health is now "+str(self.health))

    def heal(self,hp):
        self.health +=hp

    def move(self,direction, map):#player can walk north, south, east, west
        #send players move intention to the map object which will check if the move is possible i.e are they at the edge of he map?
        self.xcord, self.ycord = map.entityMove(self.xcord,self.ycord, direction, self)
        print("your players position is Y: " + str(self.ycord) + " X: "+ str(self.xcord))

