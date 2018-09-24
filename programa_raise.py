#!/usr/bin/python3

# este programa serve para mostrar o raise ]

try:
    ling = input('qual a melhor linguagem de programacao ? ')

    if ling.lower().strip() == 'python':
        print('voce acertou')
    else:
        raise ValueError('linguagem errada')
except ValueError as e:
    print('Erro: {}'.format(e))
    