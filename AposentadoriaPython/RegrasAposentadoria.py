#Imports
from datetime import *
from CalculosAuxiliares import *

completou = True

def regraPermanente(sexo,idade,contribuicao,tpEfetivo,tpCargo):
    if (sexo.upper() == 'F'):
        if( idade >=62 and contribuicao >=9125 and tpEfetivo >=3650 and tpCargo >= 1825):
            completou = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20'                )
            print('---------------------------------------')
        else: 
            completou = False
            print('Não completou os requisitos para aposentadoria na Regra Permanente')
            print('---------------------------------------')
    elif (sexo.upper() == 'M'):
        if(idade >=65 and contribuicao >=9125 and tpEfetivo >=3650 and tpCargo >=1825):
            completou = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III 3º da CF/88 c.c CE/89 c.c Art. 2º, III da LCE n. 1.354/20'                )
            print('---------------------------------------')
        else: 
            completou = False
            print('Não completou os requisitos para aposentadoria na Regra Permanente')
            print('---------------------------------------')
    else: 
        completou = False
        print('Dados inválidos')
    return completou

#A Transição 1 tem como principais parâmetros a idade mínima do funcionário e 
# a data de admissão ser até 31/12/2003
#garante ao servidor integralidade e paridade
def transicao1(sexo,idade,admissao,contribuicao,tpEfetivo,tpCargo):
    dtTransicao1 = datetime.strptime('31/12/2003', '%d/%m/%Y')
    if (sexo.upper() == 'F'):
        if(idade >=62 and contribuicao >=10950 and tpEfetivo >=7300 and tpCargo >=1825 and admissao <= dtTransicao1):
            completou = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, II, III, IV, §§ 6º, ítem 1, alínea "a", e 7º, ítem 1 da LCE n. 1.354/20')
            print('---------------------------------------')
        else: 
            completou = False
            print('Não completou os requisitos para aposentadoria na Regra de Transição 1')
            print('---------------------------------------')
    elif (sexo.upper() == 'M'):
        if(idade >=65 and contribuicao >=12775 and tpEfetivo >=7300 and tpCargo >=1825 and admissao <= dtTransicao1):
            completou = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, II, III, IV, §§ 6º, ítem 1, alínea "a", e 7º, ítem 1 da LCE n. 1.354/20')
        else: 
            completou = False 
            print('Não completou os requisitos para aposentadoria na Regra de Transição 1')  
            print('---------------------------------------')         
    else: 
        completou = False
        print('Dados inválidos')
    return completou

#A Transição 2 tem como principais parâmetros a idade mínima do funcionário e 
# a data de admissão ser até 07/03/2020 (data da reforma previdenciária)
#garante, no mínimo, 60% da média dos salários
def transicao2(sexo,idade,admissao,contribuicao,tpEfetivo,tpCargo):
    #essa função deverá verificar o ano em que estamos para determinar a idade e contribuição mínima
    #ainda não implementei essa lógica
    dtTransicao2 = datetime.strptime('07/03/2020', '%d/%m/%Y')
    if (sexo.upper() == 'F'):
        if( idade >=62 and contribuicao >=10950 and tpEfetivo >=7300 and tpCargo >=1825 and admissao <= dtTransicao2):
            completou = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, I, II, III, IV, V, §§ 1º, 2º, 6º, ítem 2, e 7º, ítem 2 da LCE n. 1.354/20')
            print('---------------------------------------')
        else: 
            completou = False
            print('Não completou os requisitos para aposentadoria na Regra de Transição 2')
            print('---------------------------------------')
    elif (sexo.upper() == 'M'):
        if(idade >=65 and contribuicao >=12775 and tpEfetivo >=7300 and tpCargo >=1825 and admissao <= dtTransicao2):
            completou = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, I, II, III, IV, V, §§ 1º, 2º, 6º, ítem 2, e 7º, ítem 2 da LCE n. 1.354/20')
            print('---------------------------------------')
        else: 
            completou = False
            print('Não completou os requisitos para aposentadoria na Regra de Transição 2')
            print('---------------------------------------')
    else: 
        completou = False
        print('Dados inválidos')
    return completou

#A Transição 3 tem como parâmetro o pedágio de 100% do tempo que faltava até 07/03/2020
#Deve verificar se a data de admissão for até 31/12/2003 para garantir integralidade e paridade
def transicao3(sexo,idade,admissao,contribuicao,tpEfetivo,tpCargo,primeiroEmprego):
    dtTransicao3 = datetime.strptime('31/12/2003', '%d/%m/%Y')    
    if (sexo.upper() == 'F'):        
        if( idade >=57 and contribuicao >=10950 and tpEfetivo >=7300 and tpCargo >=1825 and admissao <= dtTransicao3):
            completou = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, I, II, III, IV, V, §§ 1º, 2º, 6º, ítem 2, e 7º, ítem 2 da LCE n. 1.354/20')
            print('---------------------------------------')
        else: 
            print('Não completou os requisitos para aposentadoria na Regra de Transição 3')
            calcPedagio(primeiroEmprego, sexo)
            print('---------------------------------------')
            completou = False
    elif (sexo.upper() == 'M'):        
        if(idade >=60 and contribuicao >=12775 and tpEfetivo >=7300 and tpCargo >=1825 and admissao <= dtTransicao3):
            completou = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 10, I, II, III, IV, V, §§ 1º, 2º, 6º, ítem 2, e 7º, ítem 2 da LCE n. 1.354/20')
            print('---------------------------------------')
        else: 
            print('Não completou os requisitos para aposentadoria na Regra de Transição 3')
            calcPedagio(primeiroEmprego, sexo)
            print('---------------------------------------')
            completou = False            
    else: 
        completou = False
        print('Dados inválidos')
    return completou

#A Transição 4 tem como parâmetro o pedágio de 100% do tempo que faltava até 07/03/2020
#Deve verificar se a data de admissão for até 07/03/2020 para garantir 100% da média dos salários
def transicao4(sexo,idade,admissao,contribuicao,tpEfetivo,tpCargo,primeiroEmprego):
    dtTransicao4 = datetime.strptime('07/03/2020', '%d/%m/%Y')    
    if (sexo.upper() == 'F'):        
        if( idade >=57 and contribuicao >=10950 and tpEfetivo >=7300 and tpCargo >=1825 and admissao <= dtTransicao4):
            completou = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 11, I, II, III, IV, V, §§ 2º, ítem 2 e 3º, ítem 2 da LCE n. 1.354/20')
            print('---------------------------------------')
        else: 
            print('Não completou os requisitos para aposentadoria na Regra de Transição 4')
            calcPedagio(primeiroEmprego, sexo)
            print('---------------------------------------')
            completou = False            
    elif (sexo.upper() == 'M'):        
        if(idade >=60 and contribuicao >=12775 and tpEfetivo >=7300 and tpCargo >=1825 and admissao <= dtTransicao4):
            completou = True
            print('Completou todos os requisitos aposentar no Art. 40, §§ 1º, III e 3º da CF/88 c.c CE/89 c.c Art. 11, I, II, III, IV, V, §§ 2º, ítem 2 e 3º, ítem 2 da LCE n. 1.354/20')
            print('---------------------------------------')
        else: 
            print('Não completou os requisitos para aposentadoria na Regra de Transição 4')
            calcPedagio(primeiroEmprego, sexo)
            print('---------------------------------------')
            completou = False            
    else: 
        completou = False
        print('Dados inválidos')    
    return completou
