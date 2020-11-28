import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt

 
def converterParaJson(lista):
    return json.dumps(lista, default=lambda o: o.__dict__, sort_keys=True, indent=4)  
  
def ConverterDeJson(objeto):
    return json.loads(objeto)        
 
def limpar(): 
    try:
        from IPython import get_ipython
        get_ipython().magic('clear')
    except:
        pass

def cadastrarProjeto():
    print("Cadastrar Projeto")
    id = int(input("Digite o id do projeto: "))
    nome = input("Digite o nome do projeto: ")
    
    projeto = [id,nome]
    
    listaProjetos.append(projeto)
    str = json.dumps(listaProjetos)
    f = open("projetos.json", "w")
    f.write(str)
    f.close()

    

def listarProjetos():
    print("Listando Projetos\n");
    print(pd.DataFrame(listaProjetos, columns=['Id','Nome']).to_string(index=False))



def projetos():
    while(True):
        print("\nProjetos\n");
        print("MENU")
        print("1 - Listar")
        print("2 - Cadastrar")
        print("3 - Exibir Gráfico")
        print("0 - Voltar")
        opcao = int(input("Digite a Opção: "))
        if(opcao == 0):
            break
        elif(opcao == 1):
            listarProjetos()
        elif(opcao == 2):
            cadastrarProjeto()
        elif(opcao == 3):
            criaGraficoProjeto()
    
def cadastrarMarcacao():
    print("Cadastrar Marcação")
    id = int(input("Digite o id do projeto: "))
    horaInicio = input("Digite a hora de início da marcação: ")
    horaTermino = input("Digite a hora de término da marcação: ")
    
    marcacao = [id,horaInicio,horaTermino ]
    
    listaMarcacoes.append(marcacao)
    str = json.dumps(listaMarcacoes)
    f = open("marcacoes.json", "w")
    f.write(str)
    f.close()


def criaGraficoProjeto():
    listaDeInformacoes = []
    for projeto in listaProjetos:
        informacoesDoProjeto = [projeto[1], 0]
        for marcacao in listaMarcacoes:
            if(projeto[0] == marcacao[0]):
                horaInicio = datetime.datetime.strptime(marcacao[1], '%H:%M')
                horaTermino = datetime.datetime.strptime(marcacao[2], '%H:%M')
                tempo = horaTermino - horaInicio
                datetime.timedelta(0, 32400)
                tempo.total_seconds()
                tempoEmHoras = tempo.total_seconds() / 60 / 60
                informacoesDoProjeto[1] = informacoesDoProjeto[1] + tempoEmHoras
        listaDeInformacoes.append(informacoesDoProjeto)
        
    projetos = [info[0] for info in listaDeInformacoes]
    horas = [info[1] for info in listaDeInformacoes]
    plt.bar(projetos, horas, 0.5, color="red")
    plt.xlabel('Projetos')
    plt.ylabel('Horas')
    plt.title('Gráfico de Barras')
    plt.show()
    

def listarMarcacoes():
    print("Listando Marcações\n");
    print(pd.DataFrame(listaMarcacoes, columns=['Id do Projeto','Horário de Inicio', 'Horário de Término']).to_string(index=False))        
    
def marcacoes():
    while(True):
        print("\nMarcações\n");
        print("MENU")
        print("1 - Listar")
        print("2 - Cadastrar")
        print("0 - Voltar")
        opcao = int(input("Digite a Opção: "))
        if(opcao == 0):
            break
        elif(opcao == 1):
            listarMarcacoes()
        elif(opcao == 2):
            cadastrarMarcacao()

def menu():
    while(True):
        print("\nGerenciamento de Projetos\n")
        print("MENU")
        print("1 - Projetos")
        print("2 - Marcações")
        print("0 - Sair")
        opcao = int(input("Digite a Opção: "))
        if(opcao == 0):
            break
        elif(opcao == 1):
            projetos()
        elif(opcao == 2):
            marcacoes()
 
def carregarProjetos():
    try:
        f = open("projetos.json", "r")
        listaStr = json.loads(f.read())
        f.close()
        return listaStr
    except:
        return []
    
def carregarMarcacoes():
    try:
        f = open("marcacoes.json", "r")
        listaStr = json.loads(f.read())
        f.close()
        return listaStr
    except:
        return []
           
listaProjetos = carregarProjetos()    
listaMarcacoes = carregarMarcacoes()       
                    
menu()