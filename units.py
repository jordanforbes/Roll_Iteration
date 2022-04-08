from utility import p,v,hp,sc,s,klax
from dice import Dice as D



class Unit:
    def __init__(self,hp=0, atk=0):
        self.hp=hp
        self.atk=atk
        
    def attack(self,t):
        t.damage(self.atk)
        
    @property
    def getHP(self):
        return self.hp
    
    def setHP(self,v):
        self.hp -= v
    
    def heal(self,v):
        self.hp += v 
    
    def damage(self,v):
        self.hp -= v
        
    
    
        
#player class
class Player(Unit):
    def __init__(self,hp=10,atk=3, name="Player"):
        self.name = name
        super().__init__(hp,atk)
        
    def attack(self,t):
        t.damage(self.atk)
        p(self.name+" attacked "+t.name+ " for "+s(self.atk)+" damage")

#enemy class
class Enemy(Unit):
    
    def __init__(self,hp= 5,atk=1, name="bad guy"):
        self.name=name
        super().__init__(hp,atk)
    
    def attack(self,t):
        t.damage(self.atk)
        p(self.name+" attacked "+t.name+ " for "+s(self.atk)+" damage")
        
### TEST ###

# def hpTest(u):
#     p("initial hp")
#     u.getHP
#     u.heal(3)
#     p("3 heal")
#     u.getHP
#     u.damage(3)
#     p("3 damage")
#     u.getHP


# def uTest():
    
#     p1= Player()
#     e1= Enemy()
#     u1= Unit()
    
#     klax("player hpTest: ")
#     hpTest(p1)
#     klax("enemy hpTest: ")
#     hpTest(e1)
#     klax("unit hpTest: ")
#     hpTest(u1)
#     if v(p1)==v(p1):
#         p("Test 1 passed")
#     else:
#         p("Test 1 failed")
#         return False 



 
# uTest()

