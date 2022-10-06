import funcoes

while True:
    cnpj = funcoes.retirar_pontuacao(input('\nQual o CNPJ? \n')) 
    novo_cnpj = cnpj[:-2]
    cod_validacao = "6543298765432"

    novo_cnpj += funcoes.primeiro_digito(novo_cnpj, cod_validacao)
    novo_cnpj += funcoes.segundo_digito(novo_cnpj, cod_validacao)
    funcoes.validacao(cnpj, novo_cnpj)