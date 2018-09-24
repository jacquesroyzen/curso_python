#!/usr/bin/python3


#maneira 1
# arquivo = open('nomes.txt', 'w')
# arquivo.write('Pedro')
# arquivo.close()


# with open('nomes.txt', 'a') as arq:
#      arq.write('Pedro\n')
#      arq.write('joao\n')

# nomes = ['pedro\n', 'joao\n', 'maria\n']
# with open('nomes.txt', 'w') as arq:
#      arq.writelines(nomes)



# # leitura
# with open('nomes.txt', 'r' ) as arq:
#     conteudo = arq.readlines()
# print(conteudo)

# #leitura sequencial
# with open('nomes.txt', 'r' ) as arq:
#     print(arq.readline())
#     print(arq.readline())
#     arq.seek(0)
#     print(arq.readline())

# # pra fazer sequencial joga para uma lista 
# nomes = ['pedro','joao','maria','carlos']
# with open('nomes.txt', 'w' ) as arq:
#     conteudo = arq.readlines()
    
# for x in conteudo:
#     print(x, end='') 
#     pula = x + '/n'

# # pra fazer sequencial joga para uma lista 
# nomes = ['pedro','joao','maria','carlos']
# with open('nomes.txt', 'w' ) as arq:
#     for nome in nomes:
#         arq.write(nome+'\n')

# #manipulando a lista primeiro
# nomes = ['pedro','joao','maria','carlos']
# aux = [x+'\n' for x in nomes]

# with open('nomes.txt', 'w') as arq:
#     arq.writelines(aux)


# exercicio para numerar 
with open('nomes.txt', 'r' ) as arq:
    conteudo = arq.readlines()
cont = 0
with open('nomes.txt', 'w' ) as arq1:
    for cont,linha in enumerate(conteudo):
        #    linha_comp = str(cont) + '-' + linha 
        linha_comp = '{} - {}'.format(cont+1, linha)
        print(linha_comp)
        arq1.write(linha_comp)

#############################################################################










