#!/usr/bin/python3
class Dog():
#instancia
        ''' tentando fazer um dog'''
        def __init__(self, nome, idade, raca):
            self.nome = nome
            self.idade = idade
            self.raca = raca
            self.energia = 3


# reescrevendo o _str_ que originalmente traz o endereco de memoria
        def __str__(self):
            return 'nome:{}, idade:{}, raca:{}'.format(
                self.nome, self.idade, self.raca
            )


        def latir(self):
            self.energia -= 1
            print('uauauau {}'.format(self.energia))

        def dormir(self):
            self.energia = 3
            print('zzzzzzz...{}'.format(self.energia))

        
        def renomear(self, new):
            self.nome = new

#cria o objeto 1
dog1 = Dog('bilu',2,'pitbull')
dog2 = Dog('rex', 1, 'poodle')

#lista todos os metodos e atribultos
# print(dir(dog1))

#dunder doc mostra aquele texto lá em cima "tentando fazer um dog"
# print(dog1.__doc__)


print(dog1)
print(dog2)

dog1.latir()
dog1.latir()
dog1.latir()

dog1.dormir()
dog1.latir()

dog1.renomear('python')

print(dog1.nome)
