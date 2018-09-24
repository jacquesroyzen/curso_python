#!/usr/bin/python3
# par = []
# # numeros = [12,15,18,19,23,24]

# # for x in numeros:
# #     if x % 2 == 0:
# #         par.append(x)
# # print(par)
# ############ outro jeito 
# numeros = [12,15,18,19,23,24]
# par = [x for x in numeros if x % 2 == 0]
# print(par)

# numero = input('Qual o numero: ')
# num = 0
# while num <= int(numero):
    
#     num = num + 1
#     if num % 2 == 0:
#         print(num)

# dic1 = {"jacques":53,"bia":51,"leticia":16}
# print(dic1)
# for item in dic1:
#     print(item) 
# print(format(dic1))

def calculo(x:int,y:int)->int:
    return ((x**2 + y)/(y-2))

print(calculo(4,3))

