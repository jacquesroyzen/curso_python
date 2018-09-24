#!/usr/bin/python3

# a = lambda x, y: x+y
# print(a(2,5))

# # Este é um exemplo onde ela é chamada direto e o 3 é o parametro. 
# print((lambda x: x*2)(3))

# def soma(x,y): return x+y

for x in range(1, 11,1):
    print((lambda y: y**2)(x))

x = 1
quadrado = []
while x < 11:
    print((lambda x: x**2)(x))
    quadrado.append((lambda y: y**2)(x))
    x = x + 1
print(quadrado)

# funcao MAP 
#################################################################################
print(list(map(lambda x: x**2, range(1,101))))
###################################################################################
nomes = ['daniel', 'maria', 'jacques']

#title transforma o primeiro caracter em maiusculo
print(list(map(lambda x:x.title(),nomes)))




# cont = 1
# while cont < 11:
# # o pass ignora o que tem dentro, pois se estiver vazio dá erro.
# # usado em uma funcao que está prevista as nao está pronta ainda. 
#     pass
# #print(cont)