# try:
#     n1 = float(input('digite nota 1: '))
#     n2 = float(input('digite nota 2: '))

#     media = ( n1 + n2 ) / 2
#     if media >= 7:
#         status = 'Aprovado' 
#     elif media > 3 and media < 7:
#         status = 'recuperacao'
#     else:
#         status = 'reprovado'

#     mensagem = 'sua média foi de {0} portanto você foi {1}'.format(media,status)
#     print(mensagem)
# except Exception:
#     print('deu ruim')

# finally:
#     print('eu sempre estou aqui')

# ####################################################################################
# try:
#     n1 = float(input('digite nota 1: '))
# except Exception:
#     print('deu ruim')
#     exit()
# ##############################################################################
# try:
#     n1 = float(input('digite nota 1: '))
# except Exception as e:
#     print('ERRO {}'.format(e))
#     exit()

##################################################################################

nomes = ['daniel', 'jacques','joao','cleusa']
try:
    convidado = input('digite o codigo do convidado: ')
    conv = nomes[int(convidado)]
    print(conv)
except  IndexError as e:
    print('este convidado está fora da lista : {}'.format(convidado))
    exit()

