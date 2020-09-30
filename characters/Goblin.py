class Goblin():
    def __init__(self,x,y):
        self.ycord = y
        self.xcord = x
        self.health = 10
        self.armor = 5
        self.strength = 1

    def damage(self,hp):
        self.health -= hp
    def heal(self,hp):
        self.health +=hp
    def attack(self):
        pass