import PySimpleGUI as sg
from utility import p,v,hp,sc,s,klax

from units import Unit,Player,Enemy


class GUI:

    @staticmethod
    def init(player,enemy): 

        layout=[
                [sg.Button("player attack enemy", k='-PATKE-')], 
                [sg.Text("player hp: "+s(player.getHP),k='-PLAYERHP-')],
                [sg.Text("enemy hp: "+s(enemy.getHP),k='-ENEMYHP-')],
                [sg.Button("enemy attack player", k="-EATKP-")],
                ]


        win = sg.Window('Roll').Layout(layout)

        while player.getHP>0:
            #event, values
            e, v = win.Read() 
            
            if e == sg.WIN_CLOSED or e == 'Close':
                break 
            
            if e == '-PATKE-':
                player.attack(enemy)
                win['-ENEMYHP-'].update("enemy hp: "+s(enemy.getHP))
            
            if e == '-EATKP-':
                enemy.attack(player)
                win['-PLAYERHP-'].update("player hp: "+s(player.getHP))

        win.Close()
        
### TEST ###

pt = Player()
et = Enemy()
ut= Unit()
G = GUI()
G.init(pt,et)


