import json
import os

Python_Dir = os.path.dirname(os.path.abspath(__file__))
Data = os.path.join(Python_Dir, 'Data.json')

with open(Data, 'r') as arquivo_json:
    dados_lidos = json.load(arquivo_json)
    
#Adicionar contato   
#Tel = input("telefone ")
#name = input("nome ")
#dados_lidos[Tel] = name

print(dados_lidos)

#Deletar
#Del = input("deletar nome ")
#del dados_lidos[Del in dados_lidos.values()]
#print(dados_lidos)

#modificar

digite = input('tel ')

if digite in dados_lidos.keys():
    dados_lidos[digite] = "1111"

print(dados_lidos)
    
