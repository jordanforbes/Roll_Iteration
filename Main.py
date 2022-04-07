from utility import p,v,hp,sc,s,klax
import units as u
from DiceClass import D
import PySimpleGUI as sg

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

###gui###
i=0

layout=[
        [sg.Text( "hello" )],
        [sg.Text( i, k='-int-' )],
        [sg.Button( "Foo", k='-FOO-' )]
        ]

while hp(e1)>0:
    turn+=1
    p("turn "+s(turn))
    p1.attack(e1)
    p("==end turn==")
    p()
    sc(p1,e1)
    p()

win = sg.Window('Roll').Layout(layout)

while True:
    #event, values
    e, v = win.Read() 
    
    if e == sg.WIN_CLOSED or e == 'Close':
        break 
    
    if e == '-FOO-':
        i+=1
        win['-int-'].update(i)

win.Close()
  
###gui###  

klax("########")
klax("GAMEOVER")
klax("########")
