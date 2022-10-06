import funcoes

cod_validacao = "6543298765432"


while True:
    novo_cnpj = funcoes.gerador()
    novo_cnpj += funcoes.primeiro_digito(novo_cnpj, cod_validacao)
    novo_cnpj += funcoes.segundo_digito(novo_cnpj, cod_validacao)
    funcoes.acrescentar_pontuacao(novo_cnpj)