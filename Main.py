from utility import p,v,hp,sc,s,klax
import units as u
from DiceClass import D

#instantiate units, variables          
p1,e1= u.Player(),u.Enemy()


#debug units
#p(e1.hp)
#hp(e1)

#game loop
#hp=hp(p1)
turn=0
klax("#####")
klax("START")
klax("#####")
p()
sc(p1,e1)
p()
while hp(e1)>0:
    turn+=1
    p("turn "+s(turn))
    p1.attack(e1)
    p("==end turn==")
    p()
    sc(p1,e1)
    p()

klax("########")
klax("GAMEOVER")
klax("########")
