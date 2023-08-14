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
Close = 0

def Fechar_Janelas():
    window_mod_M.close()
    window_mod.close()
    window_exc.close()
    window_adc.close()
    window2.close()
    window.close()


layout_Menu =[
    [sg.Input(size=(40, 5),font= ('Helvetica', 40),key='-DISPLAY-',readonly=True,justification='center')],[Mensagem],
    [sg.Button('1',**config_button), sg.Button('2',**config_button), sg.Button('3',**config_button)],
    [sg.Button('4',**config_button), sg.Button('5',**config_button), sg.Button('6',**config_button)],
    [sg.Button('7',**config_button), sg.Button('8',**config_button), sg.Button('9',**config_button)],
    [sg.Button('0',**config_button)],
    [sg.Button('Desigar',**config_button_F,button_color='red'),
    sg.Button('Limpar',**config_button_F,),sg.Button('Ligar',**config_button_F,button_color='green')],
    [sg.Text("",size=(7,5))],[sg.Button('&',**config_button_F),sg.Text("",size=(25,5)),sg.Button('Agenda',**config_button_F)]]

layout_Agenda =[[sg.Button("<",key='-Back-')],[sg.Text("",size=(5,5))],[sg.Text("Contatos",font=('Helvetica',20))],
    [sg.Text("",size=(5,1))],[sg.Button('Adicionar',**config_button_AG)],
    [sg.Button('Modificar',**config_button_AG)],
    [sg.Button('Excluir',**config_button_AG)]]

layout_adc =[[sg.Button("<",key='-Back-')],[sg.Text("",size=(5,6))],[sg.Text("Contatos",font=('Helvetica',20),size=(0,2))],
    [sg.Text("Nome   "),sg.Input(size=(40, 5),font= ('Helvetica', 25),key='-NEW_NAME-',justification='center')],
    [sg.Text("Numero"),sg.Input(size=(40, 5),font= ('Helvetica', 25),key='-NEW_TEL-',justification='center',)],
    [sg.Button("Enviar",**config_button_AG,key='-enviar-')]]

layout_exc=[[sg.Button("<",key='-Back-')],[sg.Text("",size=(5,6))],[sg.Text("Contatos",font=('Helvetica',20),size=(0,2))],
    [sg.Text("Nome   "),sg.Input(size=(40, 5),font= ('Helvetica', 25),key='-NAME_EXC-',justification='center')],
    [sg.Button("Excluir",**config_button_AG,key='-excluir-')]]

layout_mod=[[sg.Button("<",key='-Back-')],[sg.Text("",size=(5,6))],[sg.Text("Digite o nome ou telefone do contato \n que deseja modificar",font=('Helvetica',20),size=(0,2),justification='center')],[sg.Text("",size=(2,2))],
    [sg.Text("Nome   "),sg.Input(size=(30, 5),font= ('Helvetica', 25),key='-MOD_NAME-',justification='center'),sg.Button("Pesquisar",key='-modname-')],
    [sg.Text("OU")],
    [sg.Text("Numero"),sg.Input(size=(30, 5),font= ('Helvetica', 25),key='-MOD_TEL-',justification='center',),sg.Button("Pesquisar",key='-modtel-')]]




window = sg.Window("Chamada",layout_Menu,size=(600,650),element_justification='c')
window2 = sg.Window("Chamada",layout_Agenda,size=(600,650),element_justification='c',finalize=True)
window2.hide()
window_adc =sg.Window("Chamada",layout_adc,size=(600,650),element_justification='c',finalize=True,)
window_adc.hide()
window_exc =sg.Window("Chamada",layout_exc,size=(600,650),element_justification='c',finalize=True)
window_exc.hide()
window_mod =sg.Window("Chamada",layout_mod,size=(800,650),element_justification='c',finalize=True)
window_mod.hide()


while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:
        break
    elif  event == 'Agenda':
        window2.un_hide()
        window.hide()
        while True:
         evento2, valores2 = window2.read()
         if evento2 == sg.WINDOW_CLOSED: 
             Fechar_Janelas()
             break
         elif evento2 == 'Adicionar':
            window_adc.un_hide()
            window2.hide()
            while True:
                evento_adc, valores_adc = window_adc.read()
                if evento_adc == sg.WINDOW_CLOSED:
                 Fechar_Janelas()
                 break

                elif evento_adc == '-Back-':
                     window2.un_hide()
                     window_adc.hide()
                     break
                
                elif evento_adc == '-enviar-':
                 New_Name=valores_adc['-NEW_NAME-']
                 New_Tel=valores_adc['-NEW_TEL-']

                 if  New_Name == "" or New_Tel == "" or len(New_Tel) < 8:
                     sg.popup("Insira valores validos")
                     window_adc['-NEW_TEL-'].update('')
                     window_adc['-NEW_NAME-'].update('')
                     continue
                 
                 else:
                     if sc.Verificar_duplicidade(New_Tel,New_Name) == True:
                      sc.Adicionar_Contato(New_Name,New_Tel)
                      sg.popup("Contato adicionado!")
                      window_adc['-NEW_TEL-'].update('')
                      window_adc['-NEW_NAME-'].update('')
                      continue
                     
                     else:
                         sg.popup("Já existe um contato com esse número ou nome")
                         window_adc['-NEW_NAME-'].update('')
                         window_adc['-NEW_TEL-'].update('')
                 
         elif evento2 =='Modificar':
            window_mod.un_hide()
            window2.hide()
            while True:
                evento_mod, valores_mod = window_mod.read()

                if evento_mod == sg.WINDOW_CLOSED:
                 Fechar_Janelas()
                 break 

                elif evento_mod== '-Back-':
                     window2.un_hide()
                     window_mod.hide()
                     break
                
                elif evento_mod== '-modname-' or evento_mod =='-modtel-':
                       
                       Search = True
                       Name_mod = valores_mod['-MOD_NAME-']
                       Tel_mod = sc.Localizar_Contatos(valores_mod['-MOD_NAME-'])


                    layout_mod_M=[[sg.Text("",size=(5,6))],[sg.Text("Contato",font=('Helvetica',20),size=(0,2))],[sg.Text(Name_mod)],[sg.Text(Tel_mod)],
                    [sg.Button("Excluir",**config_button_AG,key='-excluir-')]]

                    window_mod_M = sg.Window("Chamada",layout_mod_M,size=(500,500),element_justification='c',finalize=True, modal=True)
                    window_mod_M.un_hide()
                    while True: 
                     evento_mod_M, valores_mod_M = window_mod_M.read()
                
                     if evento_mod_M == sg.WINDOW_CLOSED:
                      window_mod_M.close()
                      break

                                
         elif evento2 =='Excluir':
            window_exc.un_hide()
            window2.hide()

            while True:
                evento_exc, valores_exc = window_exc.read()
                if evento_exc == sg.WINDOW_CLOSED:
                 Fechar_Janelas()
                 break 

                elif evento_exc== '-Back-':
                     window2.un_hide()
                     window_exc.hide()
                     break
                
                elif evento_exc == '-excluir-':
                    Contato_Exc=valores_exc['-NAME_EXC-']
                    Excluir = sc.Excluir_Contato(Contato_Exc)

                    if Excluir == True:
                      sg.popup("Contato excluido !")
                      window_exc['-NAME_EXC-'].update('')

                    else:
                      sg.popup("Contato não encontrado")
                      window_exc['-NAME_EXC-'].update('')
             
             
         elif evento2 == '-Back-':
                     window.un_hide()
                     window2.hide()
                     break
      
    elif event == 'Limpar' and Chamada_em_andamento == False:
        valor_atual = '' 
        window['-DISPLAY-'].update(valor_atual)
                
    elif event.isdigit():
        if len(valor_atual) > 7:
            sg.popup('numero maximo atingido!')
            window['-DISPLAY-'].update(valor_atual)
        else:
         valor_atual += event 
         window['-DISPLAY-'].update(valor_atual)   
               
    elif event=='Ligar':
        Number=sc.Formatar_input(valor_atual)
        valor_atual=sc.Read_Data(Number)
        window['-DISPLAY-'].update(valor_atual)
        
        if valor_atual == None:
            sg.popup('Numero invalido')
            valor_atual='' 
            window['-DISPLAY-'].update(valor_atual)
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
        window['-DISPLAY-'].update(valor_atual)
            
    if contador_iniciado:
        tempo_decorrido = int(time.time() - tempo_inicial)
        horas = tempo_decorrido // 3600
        minutos = (tempo_decorrido % 3600) // 60
        segundos = tempo_decorrido % 60

        tempo_formatado = f'{horas:02d}:{minutos:02d}:{segundos:02d}'
        window['-TEMPO-'].update(f'Chamada em andamento: {tempo_formatado}')
Fechar_Janelas()

#Para fechar corretamente uma unica window no pysimplegui deve-se adicionar um if 
#com um break para para o loop, um break fora do loop e um window.close() fora
#do ultimo loop do código

#Novo método- atribuir o resultado sg.WINDOW_CLOSED a window.close e em seguida break



        
    
    