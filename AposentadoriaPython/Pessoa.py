# PREVISÃO PARA APOSENTADORIA

#Imports
from RegrasAposentadoria import regraPermanente, transicao1, transicao2, transicao3, transicao4
from datetime import *
from CalculosAuxiliares import *

#Definindo variáveis
nome =''
rg = ''
sexo = ''
dtNascimento = ''
cargo = ''
dtExercicio = ''
dtNivel = ''
tempoOab = 0
tempoInss = 0
tempoOutroPublico = 0

#Entradas
nome = input('Nome: ')
rg = input('RG: ')
sexo = input('Sexo (M ou F): ')
dtNascimento = input('Data Nascimento (dd/mm/aaaa): ')
cargo = input('Cargo: ')
dtExercicio = input('Início Exercício (dd/mm/aaaa): ')
dtNivel = input('Data Nível (dd/mm/aaaa): ')
tempoOab = int(input('Tempo de OAB (em dias): '))
tempoInss = int(input('Tempo de INSS (em dias): '))
tempoOutroPublico = int(input('Tempo de Outros Órgãos (em dias): '))
dtFechamento = input('Fechamento da contagem (dd/mm/aaaa): ')

#Aplicando as fórmulas auxiliares
dtNascFormat = textoParaData(dtNascimento)
dtExercFormat = textoParaData(dtExercicio)
if (dtNivel != ''):
  dtNivelFormat = textoParaData(dtNivel)
dtFechFormat = textoParaData(dtFechamento)

idade = calcIdade(dtNascFormat)
cincoAnos = cincoAnosExercicio(dtExercFormat)
dezAnos = dezAnosExercicio(dtExercFormat)
vinteAnos = vinteAnosExercicio(dtExercFormat)

totalContribuicao = tempoContribuicao(dtExercFormat,dtFechFormat,tempoOab,
                                      tempoInss,tempoOutroPublico)
tempoEfetivo = tempoContribuicao(dtExercFormat,dtFechFormat,tempoOab,
                                      0,tempoOutroPublico)
anosContribuicao = totalContribuicao/365
#pedagio = calcPedagio(dtExercFormat,sexo)
tempoNoCargo = tempoCargo(dtExercFormat,dtFechFormat,cargo,tempoOab,tempoOutroPublico)

#Testando as regras de aposentadoria
def regras():
  regraPermanente(sexo,idade,totalContribuicao,tempoEfetivo,tempoNoCargo)
  transicao1(sexo,idade,dtExercFormat,totalContribuicao,tempoEfetivo,tempoNoCargo)
  transicao2(sexo,idade,dtExercFormat,totalContribuicao,tempoEfetivo,tempoNoCargo)
  transicao3(sexo,idade,dtExercFormat,totalContribuicao,tempoEfetivo,tempoNoCargo)
  transicao4(sexo,idade,dtExercFormat,totalContribuicao,tempoEfetivo,tempoNoCargo)

#Saídas
print('---------------------------------------')
print(nome.upper())

regras()