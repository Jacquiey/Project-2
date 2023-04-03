# ID - 10984191
# DEPARTMENT - BIOMEDICAL ENGINEERING

import qrcode
import PySimpleGUI as sg

sg.theme('BlueMono')
font = ('Monaco', 18)

qr_image=[sg.Image('',key='-QRCODE-',size=(250,250),background_color='grey')]

layout=[
    [sg.Text('Enter URL:')],
    [sg.Input('',key='-URL-',justification='center')],
    [sg.Button('Create',key='-submit-',expand_x=True,button_color='red')],
    [sg.Column([qr_image],justification='center')],
]

wind = sg.Window('QRCODE Generator App',layout, font=font)

while True:
    event,values = wind.read()
    if event==sg.WIN_CLOSED:
        break
    elif event == '-submit-':
        url = values['-URL-']
        if url:
            image= qrcode.make(url)
            image.save('qr.png')
            wind['-QRCODE-'].update('qr.png')
wind.close()   