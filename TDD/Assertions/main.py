from calculadora import Soma

#print(Soma(10,20))
#print(Soma(1,2))
#print(Soma(1.5,2.5))

try:
    print(Soma('15',15))
except AssertionError as e:
    print(f'Conta inválida: {e}')