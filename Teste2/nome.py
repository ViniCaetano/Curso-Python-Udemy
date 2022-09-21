nome = input('Qual o seu nome? ')
if len(nome) <= 4:
    print('Seu nome é curto.')
elif len(nome) > 4 and len(nome) < 7:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')