
import json
import os

Python_Dir = os.path.dirname(os.path.abspath(__file__))
Data = os.path.join(Python_Dir, 'Data.json')

with open(Data, 'r') as arquivo_json:
    dados_lidos = json.load(arquivo_json)
    
#Adicionar contato   
#Tel = "1234-1234"
#name = input("nome ")
#dados_lidos[Tel] = name

#print(dados_lidos)

#Deletar
#Del = input("deletar nome ")
#if Del in dados_lidos:
#    del dados_lidos[Del]
#print(dados_lidos)

#modificar

digite = input('tel ')

if digite in dados_lidos.values():
   dados_lidos.update({digite: "1"})

print(dados_lidos)
#def encontrar_chave_por_valor(dicionario, valor_procurado):
#    for chave, valor in dicionario.items():
 #       if valor == valor_procurado:
 #           return chave
 #   return None


#digite = input('tel ')

#chave_encontrada = encontrar_chave_por_valor(dados_lidos, digite)

#print(chave_encontrada)
    
