import json
import os

Python_Dir = os.path.dirname(os.path.abspath(__file__))
Data = os.path.join(Python_Dir, 'Data.json')
nomes=''

with open(Data, 'r') as arquivo_json:
    dados_lidos = json.load(arquivo_json)

def Read_Data(Number):
    with open(Data, 'r') as arquivo_json:
         dados_lidos = json.load(arquivo_json)
    try:
      print(dados_lidos[Number])
    except KeyError as error:
      return 'Erro' 
    else:
     return str(dados_lidos[Number])


  
def Formatar_input(Number):
    if len(Number) > 4 and Number[4] != '-':
     Number = f"{Number[:4]}-{Number[4:]}"
     return Number
    

