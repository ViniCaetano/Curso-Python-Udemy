import re
from random import randint


def gerador():
    digitos = str(randint(10000000, 99999999))
    return digitos + "0001"


def acrescentar_pontuacao(novo_cnpj):
    pergunta = input('Gerar CNPJ com pontuação? \n[S] Sim \n[N] Não\n')
    if pergunta.upper() == 'S' or pergunta.upper() == 'SIM':
        print(f'{novo_cnpj[:2]}.{novo_cnpj[2:5]}.{novo_cnpj[5:8]}/{novo_cnpj[8:12]}-{novo_cnpj[12:]}\n')
    elif pergunta.upper() == 'N' or pergunta.upper() == 'NÃO':
        print(f'{novo_cnpj}\n')
    else:
        print('Digite uma opção válida: Sim ou Não.\n')
        acrescentar_pontuacao(novo_cnpj)


def retirar_pontuacao(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def primeiro_digito(novo_cnpj, cod_validacao):
    variavel = sum([int(x) * int(y) for x, y in zip (novo_cnpj, cod_validacao[1:])])
    formula = 11 - (variavel % 11)
    if formula > 9:
        digito1 = 0
    else:
        digito1 = formula
    return str(digito1)


def segundo_digito(novo_cnpj, cod_validacao):
    variavel = sum([int(x) * int(y) for x, y in zip (novo_cnpj, cod_validacao)])
    formula = 11 - (variavel % 11)
    if formula > 9:
        digito2 = 0
    else:
        digito2 = formula
    return str(digito2)


def validacao(cnpj, novo_cnpj):
    try:
        if cnpj[0] * len(cnpj) == cnpj:
            print('Número sequenciais. CNPJ inválido.')
        elif cnpj == novo_cnpj:
            print('O CNPJ é válido.')
        else:
            print('O CNPJ é inválido.')
    except:
        print('O CNPJ é inválido.')