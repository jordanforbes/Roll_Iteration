from utility import p,v,hp,sc,s,klax
import units as u
from DiceClass import D
import PySimpleGUI as sg
from gui import GUI as G

#instantiate units, variables          
p1,e1= u.Player(),u.Enemy()

### game setup ###
turn=0
klax("#####")
klax("START")
klax("#####")
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
G.initGUI()
  

### game end ###
klax("########")
klax("GAMEOVER")
klax("########")


