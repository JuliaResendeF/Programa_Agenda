import json
import os


Python_Dir = os.path.dirname(os.path.abspath(__file__))
Data = os.path.join(Python_Dir, 'Data.json')
nomes=''

with open(Data, 'r') as arquivo_json:
    dados_lidos = json.load(arquivo_json)


def Read_Data(Number):
      for chave, valor in dados_lidos.items():
        if valor == Number:
            print(chave)
            return chave
        
def Formatar_input(Number):
    if len(Number) > 4 and Number[4] != '-':
     Number = f"{Number[:4]}-{Number[4:]}"
     return Number

def Verificar_duplicidade(Tel):
    Tel = Formatar_input(Tel)
    if Tel in dados_lidos.values():
     return False
    else:
        return True

def Adicionar_Contato(New_Name,New_Tel):
     New_Tel = Formatar_input(New_Tel) 
     dados_lidos.update({New_Name: New_Tel})
     with open(Data, 'w') as arquivo:
        json.dump(dados_lidos, arquivo, indent=4)

def Excluir_Contato(Tel):
    del dados_lidos[Tel in dados_lidos.values()]
    with open(Data, 'w') as arquivo:
        json.dump(dados_lidos, arquivo, indent=4)
        

    
      
     
    

