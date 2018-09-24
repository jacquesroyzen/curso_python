#!/usr/bin/python3
class Conta():
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def sacar(self, Valor):
        self.saldo -= Valor
        return self.saldo

    def depositar(self,valor):
        self.saldo +=valor
        return self.saldo

    def transferencia(self,valor, conta ):
        self.sacar(valor) 
        conta.depositar(valor)

    def receber(self, titular, valor):
        self.saldo += valor 

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def __str__(self):
        return 'titular: {} numero: {} saldo: {} tipo: CC'.format(self.titular, self.numero, self.saldo)


# HERANCA DA CLASSE CONTA
class Poupanca(Conta):
#sobrescreve o init , fazendo um init para a poupança
    def __init__(self, titular, numero, saldo):
        # o comando super recupera o init do pai, no caso a classe Conta
        super().__init__(titular,numero,saldo)
        #depois do super você pode adicionar um atribulto novo valido para a poupanca
        self.juros =  0.005

    def render(self):
         self.saldo += self.saldo * self.juros
    def __str__(self):
        return 'titular: {} numero: {} saldo: {} tipo: Poupança'.format(self.titular, self.numero, self.saldo)



c1 = Conta('Daniel','12345',500)
c2 = Poupanca('Joao','123456',1000)
c2.render()
print(c2.saldo)


c2.transferencia(c2.saldo,c1)
# print(c1.saldo)
# print(c2.saldo)


# print(c1.saldo)
# print(c1.depositar(500))
# print(c1.saldo)
# print(c1.sacar(300))
print(c1.saldo)
print(c2.saldo)


