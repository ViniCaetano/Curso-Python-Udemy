import re

def retirar_pontuacao (cnpj):
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