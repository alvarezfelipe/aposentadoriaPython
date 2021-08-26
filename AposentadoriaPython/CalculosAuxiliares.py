#Imports
from datetime import *

#Função String para Datas
def textoParaData(a):
  b = datetime.strptime(a, '%d/%m/%Y')
  return b

#----------------------------------------------------
#Idade do Funcionário
def calcIdade(nascimento):
  hoje = date.today()
  idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
  return idade

#----------------------------------------------------
#Tempos de Efetivo Exercício
#timedelta acrescenta ou subtrai
def cincoAnosExercicio(exercicio):
    return exercicio + timedelta(days=1825)

def dezAnosExercicio(exercicio):
    return exercicio + timedelta(days=3650)

def vinteAnosExercicio(exercicio):
    return exercicio + timedelta(days=7300)


#Função Tempo de Contribuição
#Para saber tempo de EFETIVO SERVIÇO PÚBLICO, basta colocar 0 no parâmetro INSS
def tempoContribuicao(inicio,fim,oab,inss,outro):
  outros = oab+inss+outro
  qtdeDias = abs((fim - inicio).days)+1
  return outros + qtdeDias

#Função para tempo de cargo
def tempoCargo(inicio,fim,cargo,oab,outro):
    dtCargo = inicio
    nivel = ''
    if (cargo.upper() == "PROCURADOR" or cargo.upper() == "ENGENHEIRO"):
        dtCargo = nivel
        tempo = (abs((fim - dtCargo).days)+1) + oab + outro
        return tempo
    else:
        tempo = (abs((fim - dtCargo).days)+1) + outro
        return tempo

#----------------------------------------------------

#Função para cálculo de pedágio de Contribuição
def calcPedagio(admissao,sexo):    
    fimConta = datetime.strptime('07/03/2020', '%d/%m/%Y')
    dtPedagio = ''    
    tPedagio = abs((fimConta - admissao).days)+1
    faltaPedagio = 0
    if (sexo.upper() == "F"):
        if (tPedagio >=10950):
            print('Não há pedágio a ser pago.')
            print('Completou contribuição necessária até 07/03/2020')
        else:
            #dtPedagio = admissao + timedelta(days=10950)
            faltaPedagio = 10950 - tPedagio - 1
            dtPedagio = admissao + timedelta(days=10950) + timedelta(days=faltaPedagio)
            #return print(datetime.strptime(dtPedagio,'%d/%m/%Y'))
            return print('Completará o pedágio em: ' + datetime.strftime(dtPedagio, '%m/%d/%Y'))
    elif (sexo.upper() == "M"):
        if (tPedagio >=12775):
            print('Não há pedágio a ser pago.')
            print('Completou contribuição necessária até 07/03/2020')
        else:
            # dtPedagio = admissao + timedelta(days=12775)
            faltaPedagio = 12775 - tPedagio - 1
            dtPedagio = admissao + timedelta(days=12775) + timedelta(days=faltaPedagio)
            return print('Completará o pedágio em: ' + datetime.strftime(dtPedagio, '%m/%d/%Y'))
            #STRFTIME pega um datetime e printa em STRING no formato desejado
    else:
        print('Dados inválidos')