from characters.Goblin import Goblin

class Map():
    def __init__(self):
        self.genMap()
        self.loadBadies()
    def genMap(self):
        line=[]
        lines=[]
        #gen y cords
        for i in range(100):
            line.append(0)
        #gen x cords
        for i in range(100):
            lines.append(line)
        self.map = lines
    def entityMove(self,x,y,direction, player):
        if direction == "N":
            if x==0:
                print("you hit the edge of the world")
            else:
                x-=1
        elif direction == "S":
            if x==99:
                print("you hit the edge of the world")
            else:
                x+=1
        elif direction == "E":
            if y == 0:
                print("you hit the edge of the world")
            else:
                y-=1
        elif direction == "W":
            if y == 99:
                print("you hit the edge of the world")
            else:
                y+=1
        for e in self.enemies:
            if e.xcord == x and e.ycord ==y:
                player.damage(e, self)
        return x, y

    def loadBadies(self):
        self.enemies=[]
        self.enemies.append(Goblin(49,50))