import pandas as pd
import json
import datetime
import matplotlib.pyplot as plt

 
def converterParaJson(lista):
    return json.dumps(lista, default=lambda o: o.__dict__, sort_keys=True, indent=4)  
  
def ConverterDeJson(objeto):
    return json.loads(objeto)        
     
    
def cadastrarProjeto():
    print("Cadastrar Projeto")
    id = input("Digite o id do projeto: ")
    nome = input("Digite o nome do projeto: ")
    
    projeto = [id,nome]
    
    listaProjetos.append(projeto)
    f = open("projetos.csv", "w")
    f.writelines([str(projeto[0]) + ',' + projeto[1] + '\n' for projeto in listaProjetos])
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
        print("3 - Exibir Gráfico de Horas Trabalhadas por Projeto")
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
    id = input("Digite o id do projeto: ")
    horaInicio = input("Digite a hora de início da marcação: ")
    horaTermino = input("Digite a hora de término da marcação: ")
    
    marcacao = [id,horaInicio,horaTermino ]
    
    listaMarcacoes.append(marcacao)
    f = open("marcacoes.csv", "w")
    f.writelines([marcacao[0] + ',' + marcacao[1] + ',' + marcacao[2] + '\n' for marcacao in listaMarcacoes])
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

def criarGraficoPeriodoDeTrabalho():
    manha = 0
    tarde = 0
    noite = 0
    for marcacao in listaMarcacoes:
        horaInicio = datetime.datetime.strptime(marcacao[1], '%H:%M').hour
        if(horaInicio > 18):
            noite += 1
        elif(horaInicio > 12):
            tarde += 1
        elif(horaInicio > 6 ):
            manha += 1
        else:
            noite += 1
    nomes = ['Manhã', 'Tarde', 'Noite']
    valores = [manha, tarde, noite]
    total = sum(valores)
    plt.pie(valores,labels=nomes, autopct=lambda p: '{:.0f}'.format(p * total /100))
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
        print("3 - Criar grafico de período de trabalho")
        print("0 - Voltar")
        opcao = int(input("Digite a Opção: "))
        if(opcao == 0):
            break
        elif(opcao == 1):
            listarMarcacoes()
        elif(opcao == 2):
            cadastrarMarcacao()
        elif(opcao == 3):
            criarGraficoPeriodoDeTrabalho()

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
        f = open("projetos.csv", "r")        
        lista = []
        for linha in f.readlines():
            linha = linha.replace('\n', '')
            valores = linha.split(',')
            lista.append(valores)
        f.close()
        return lista
    except:
        return []
    
def carregarMarcacoes():
    try:
        f = open("marcacoes.csv", "r")        
        lista = []
        for linha in f.readlines():
            linha = linha.replace('\n', '')
            valores = linha.split(',')
            lista.append(valores)
        f.close()
        return lista
    except:
        return []
           
listaProjetos = carregarProjetos()    
listaMarcacoes = carregarMarcacoes()       
                    
menu()