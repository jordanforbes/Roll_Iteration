from utility import p,v,hp,sc,s,klax,title
import units as U
from gui import GUI

# instantiate units, variables          
p1,e1= U.Player(),U.Enemy()

### game setup ###
turn=0
title("GAMESTART")
p()
sc(p1,e1)
p()

### game loop ###
while hp(e1)>0:
    turn+=1
    p("turn "+s(turn))
    p1.attack(e1)
    p("==end turn==")
    p()
    sc(p1,e1)
    p()

### gui ###
GUI.init()
  

### game end ###
title("GAMEOVER")



