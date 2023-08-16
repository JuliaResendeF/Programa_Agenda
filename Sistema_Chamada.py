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

def Verificar_duplicidade(Tel,Name):
    Tel = Formatar_input(Tel)
    if Tel in dados_lidos.values() or Name in dados_lidos.keys():
      return False
    else:
        return True

def Adicionar_Contato(New_Name,New_Tel):
     New_Tel = Formatar_input(New_Tel) 
     dados_lidos.update({New_Name: New_Tel})
     with open(Data, 'w') as arquivo:
        json.dump(dados_lidos, arquivo, indent=4)

def Excluir_Contato(Tel):
    if Tel in dados_lidos:
          del dados_lidos[Tel]
          with open(Data, 'w') as arquivo:
            json.dump(dados_lidos, arquivo, indent=4)
            return True
    else:
        return False

def Localizar_Contatos_N(Pesquisa):
     for chave, valor in dados_lidos.items():
        if chave == Pesquisa:
            return valor
          
def Localizar_Contatos_T(Pesquisa):
     Pesquisa = Formatar_input(Pesquisa)
     for chave, valor in dados_lidos.items():
        if valor == Pesquisa:
            return chave

def New_mod_name (name,Tel_mod,Name_mod):
    if Tel_mod in dados_lidos.values():
       Tel_mod = dados_lidos[Name_mod]
       dados_lidos[name] = Tel_mod
    del dados_lidos[Name_mod]
    with open(Data, 'w') as arquivo:
        json.dump(dados_lidos, arquivo, indent=4)
        
def New_mod_tel (Tel_mod,Name_mod):
    if Name_mod in dados_lidos.keys():
       dados_lidos[Name_mod] = Tel_mod
    with open(Data, 'w') as arquivo:
        json.dump(dados_lidos, arquivo, indent=4)

      
        
   

        

    
      
     
    

