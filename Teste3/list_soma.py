from itertools import zip_longest

lista1 = [1,2,3,4,5,6,7,8]
lista2 = [1.5,2.5,3,4,5]

#Somando com o zip, considerando apenas os itens até o tamanho da menor lista.

lista_soma = [a + b for a, b in zip (lista1, lista2)]

print(lista_soma)

#Somando com o zilp_longest, considerando todos os itens das duas listas e atribuindo o valor 0 para os itens que faltam na lista menor.

lista_soma = [a + b for a, b in zip_longest (lista1, lista2, fillvalue = 0)]
print(lista_soma)