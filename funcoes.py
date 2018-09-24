#!/usr/bin/python3
##########################################################
# tipos de funcoes

def soma(x:int,y:int)->int:
    '''função que soma dos numeros'''
    print(x + y)


soma(4.8,8)

###############################################################

# def soma(x:int,y:int)->int:
#     '''função que soma dos numeros'''
#     return x + y

# print(soma(4,8))
# print(soma(soma(1,5),soma(8,9)))

#######################################################################
# def ler_arquivo(nome):
#         with open(nome, 'r') as arq:
#             return arq.read()
# print(ler_arquivo('nomes.txt'), sep='\n')
##########################################################################

# var = 20

# def escopo():
#     var = 5
#     print(var)
#     return var

# a = escopo()
# print(a)
# print(var)
################################################################################
# valor default 
# def boas_vindas(nome='anonimo'):
#     return 'ola seja bem vindo ' + nome

# print(boas_vindas())

###############################################################################
#funcao com parametro nomeado

# def boas_vindas(nome,sobrenome):
#     return 'ola seja bem vindo ' + nome + sobrenome

# print(boas_vindas(sobrenome='royzen',nome='jacques '))

################################################################################

# def ler_arquivo(nome):
#         with open(nome, 'r') as arq:
#             return arq.readlines()
# cont = len(ler_arquivo('nomes.txt'))
# print(cont)

#############################################################################
# def convidados(*args):
#     for nome in args:
#         print('seja bem vindo' + nome)
# convidados('damiel','joao','pedro')
#################################################################################

def convidados(**kargs):
    print(kargs)
    

convidados(nome='daniel', sobrenome='prata', cidade='sao paulo')

convidad = {"nome":"daniel","sobrenome":"prata","cidade":"sao paulo"}

# for conv in convidad:
#     print(conv) 

#####################################################################################

