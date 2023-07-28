import PySimpleGUI as sg
import Sistema_Chamada as sc
import time

config_button={ 'size': (5,2), 'font':('Helvetica', 15),}
config_button_AG={ 'size': (20,2), 'font':('Helvetica', 15),}
config_button_F={'size': (10,2), 'font':('Helvetica', 15)}
Mensagem=sg.Text('',key='-TEMPO-',font=('Helvetica', 15))

sg.set_options(font=('Helvetica', 15))
contador_iniciado = False
tempo_inicial = 0
Chamada_em_andamento= False
valor_atual = ''

layout_Menu =[
    [sg.Input(size=(40, 5),font= ('Helvetica', 40),key='-DISPLAY-',readonly=True,justification='center')],[Mensagem],
    [sg.Button('1',**config_button), sg.Button('2',**config_button), sg.Button('3',**config_button)],
    [sg.Button('4',**config_button), sg.Button('5',**config_button), sg.Button('6',**config_button)],
    [sg.Button('7',**config_button), sg.Button('8',**config_button), sg.Button('9',**config_button)],
    [sg.Button('0',**config_button)],
    [sg.Button('Desigar',**config_button_F,button_color='red'),
    sg.Button('Limpar',**config_button_F,),sg.Button('Ligar',**config_button_F,button_color='green')]]

window = sg.Window("Chamada",layout_Menu,size=(600,650),element_justification='c')

while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
    
    elif  event == 'Agenda':
        sg.popup(sc.ledados())
    
    elif event == 'Limpar' and Chamada_em_andamento == False:
        valor_atual = '' 
                
    elif event.isdigit():
        if len(valor_atual) > 7:
            sg.popup('numero maximo atingido!')
        else:
         valor_atual += event    
               
    elif event=='Ligar':
        Number=sc.Formatar_input(valor_atual)
        valor_atual=sc.Read_Data(Number)
        
        if valor_atual == 'Erro':
            sg.popup('Numero invalido')
            valor_atual='' 
        else:
            contador_iniciado = True
            tempo_inicial = time.time()
            Chamada_em_andamento= True
    
    elif event =='Desigar':
        valor_atual = ''
        contador_iniciado = False
        tempo_inicial = 0
        window['-TEMPO-'].update('')
        Chamada_em_andamento= False
            
    if contador_iniciado:
        tempo_decorrido = int(time.time() - tempo_inicial)
        horas = tempo_decorrido // 3600
        minutos = (tempo_decorrido % 3600) // 60
        segundos = tempo_decorrido % 60

        tempo_formatado = f'{horas:02d}:{minutos:02d}:{segundos:02d}'
        window['-TEMPO-'].update(f'Chamada em andamento: {tempo_formatado}')

    window['-DISPLAY-'].update(valor_atual)
     
window.close()

        
    
    