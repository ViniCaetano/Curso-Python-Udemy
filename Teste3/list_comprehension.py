string = '012345678901234567890123456789012345678901234567890123456789'

lista1 = [string[indice:indice + 10] for indice in range (0, len(string), 10)]

lista2 = '.'.join(lista1)

print(lista1)
print(lista2)