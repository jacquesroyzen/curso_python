#!/usr/bin/python3
# msg = 'hello world'
# nome = input('digite seu nome: ')
# sobrenome = 'royzen'
# print(nome, sobrenome, sep=";", end='\n\n\n\n')
# nome, idade = 'jacques',63
# mensagem = 'o nome dele é {0} e a idade é {1}'.format(nome,idade)
# print(mensagem)
# ########################################################################################
# n1 = float(input('digite nota 1: '))
# n2 = float(input('digite nota 2: '))

# media = ( n1 + n2 ) / 2
# if media >= 7:
#     status = 'Aprovado' 
# elif media > 3 and media < 7:
#     status = 'recuperacao'
# else:
#     status = 'reprovado'


# mensagem = 'sua média foi de {0} portanto você foi {1}'.format(media,status)
# print(mensagem)
# ###########################################################################################
# notas = int(input("Digite numero de notas: "))
# soma = 0
# for x in range(notas):
#      nota = int(input("digite n{} :".format(x+1)))
#      soma = soma + nota
# media = soma / notas
# print(media)
###########################################################################################
# from time import sleep
# n = 1
# while n < 100:
#     print('numero {0}'.format(n))
#     n = n + 1
#    sleep(3)
############################################################################################
# frutas = ["laranja","uva","melancia"]

# for f in frutas:
#     print (f)

##########################################################################################

#numeros = list(range(100,50,-2))
#print(numeros)

############################################################################################
# letras = []
# for x in range(100, 150,1):
# #    print(x)
# #    letras.append(chr(x))
#     letras.append(x)

# print(letras)

############################################################################################
# par = []
# numeros = [12,15,18,19,23,24]

# for x in numeros:
#     if x % 2 == 0:
#         par.append(x)
# print(par)
# ############ outro jeito 
# numeros = [12,15,18,19,23,24]
# par = [x for x in numeros if x % 2 == 0]
##########################################################################################

matriz = [[1,3,6],[3,5,7],[6,9,11]]
cont = 0
soma_total = 0
for mtz in matriz:
    cont = cont + 1
    cont_int = 0
    if cont % 2 == 0:
        for it_comp in mtz:
            cont_int = cont_int + 1
            if cont_int % 2 == 0:
                soma_total = soma_total + int(it_comp)
    else:
        for it_comp in mtz:
            cont_int = cont_int + 1
            if cont_int % 2 != 0:
                soma_total = soma_total + int(it_comp)
mensagem = 'A somatória dos eixos foi de {0}'.format(soma_total)
print(soma_total)