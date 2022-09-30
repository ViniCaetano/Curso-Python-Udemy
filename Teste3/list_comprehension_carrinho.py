carrinho = []

carrinho.append(('Produto 1', 50))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 10))

carrinho = sum([b for a,b in carrinho])

print(carrinho)