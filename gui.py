import PySimpleGUI as sg
from utility import p,v,hp,sc,s,klax


class GUI:
    
    @staticmethod
    def initGUI():
        i=0

        layout=[
                [sg.Text( "hello" )],
                [sg.Text( i, k='-int-' )],
                [sg.Button( "Foo", k='-FOO-' )]
                ]


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
        
