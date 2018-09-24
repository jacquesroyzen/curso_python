#!/usr/bin/python3
nomes = ['MARIA','JOAO','CLAUDIO','JACQUES','BIA','LETICIA']
busca = input('Qual é o nome ?')

for nome in nomes:
    if nome == busca.strip().upper():
        print('achei o nome {}'.format(nome))
        break
else:
        print ('nao achei')
        