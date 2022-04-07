from utility import p,v,hp,sc,s,klax
from DiceClass import D



class Unit:
    def __init__(self,hp=0, atk=0):
        self.hp=hp
        self.atk=atk
        
    def attack(self,t):
        t.hp -= self.atk
        
        

class Player(Unit):
    def __init__(self,hp=10,atk=3):
        self.name="Player"
        super().__init__(hp,atk)
    def attack(self,t):
        t.hp -= self.atk
        p(self.name+" attacked "+t.name+ "for "+s(self.atk)+" damage")

class Enemy(Unit):
    
    def __init__(self,hp= 5,atk=1):
        self.name="bad guy"
        super().__init__(hp,atk)