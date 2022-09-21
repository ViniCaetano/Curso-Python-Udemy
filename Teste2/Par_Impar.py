numero = input('Insira um número inteiro: ')
if numero.isnumeric():
    numero=int(numero)
    if (numero%2) == 0:
        print('O numero digitado é par.')
    else:
        print('O número digitado é impar.')
else:
    print('O número digitado não é inteiro.')