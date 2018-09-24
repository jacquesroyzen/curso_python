from unittest import TestCase, main
def raiz(num):
    return num ** 0.5
    
class Teste(TestCase):
    def test_raiz(self):
        self.assertEqual(raiz(64), 8)
        self.assertEqual(raiz(25), 5)
        self.assertLess(raiz(81), 10)


# Garante que este arquivo será executado quando for chamado direto
#se for chamado por outro ele nao executa
if __name__ == '__main__':
    main()