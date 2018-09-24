from unittest import TestCase, main

def validar_impar(num:int) -> bool:
    """Função para validar se é número ímpar"""
    if isinstance(num, int):
        return True if num % 2 != 0 else False
    elif isinstance(num, str) and num.isnumeric():
        return True if int(num) % 2 != 0 else False
    else:
        return None
    
       

class Teste(TestCase):
    def tes_impar(self):
        self.assertEqual(validar_impar(3), True)
        self.assertEqual(validar_impar(2), False)
        self.assertEqual(validar_impar(2121), True)
        self.assertEqual(validar_impar(421212), False)
        self.assertEqual(validar_impar('a'), none)

print(validar_impar.__doc__)

if __name__ == '__main__':
        main()