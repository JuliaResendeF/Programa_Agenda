import PySimpleGUI as sg

layout1 = [
    [sg.Text('Janela 1')],
    [sg.Button('Abrir Janela 2'), sg.Button('Sair')]
]

layout2 = [
    [sg.Text('Janela 2')],
    [sg.Button('Fechar Janela 2')]
]

window1 = sg.Window('Janela 1', layout1)

while True:
    event1, values1 = window1.read()

    if event1 == sg.WINDOW_CLOSED or event1 == 'Sair':
        window1.close()
        break
    elif event1 == 'Abrir Janela 2':
        window1.hide()
        window2 = sg.Window('Janela 2', layout2)

        while True:
            event2, values2 = window2.read()

            if event2 == sg.WINDOW_CLOSED or event2 == 'Fechar Janela 2':
                window2.close()
                window1.un_hide()
                break

sg.popup_animated(None)
