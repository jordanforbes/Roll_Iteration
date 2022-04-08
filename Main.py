from utility import p,v,hp,sc,s,klax,title
import units as U
from gui import GUI

# instantiate units, variables          
p1,e1= U.Player(),U.Enemy()

### game setup ###
title("GAMESTART")


### gui ###
GUI.init(p1,e1)
  

### game end ###
title("GAMEOVER")



