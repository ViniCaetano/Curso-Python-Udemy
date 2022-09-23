CPF = input('Digite o número de um CPF: ')

Soma1 = (int(CPF[0])) * 10 + (int(CPF[1])) * 9 + (int(CPF[2])) * 8 + (int(CPF[3])) * 7 + (int(CPF[4])) * 6 + (int(CPF[5])) * 5 + (int(CPF[6])) * 4 + (int(CPF[7])) * 3 + (int(CPF[8])) * 2

Digito1 = 11 - (Soma1 % 11)

if Digito1 > 9:
    Digito1 = 0

Soma2 = (int(CPF[0])) * 11 + (int(CPF[1])) * 10 + (int(CPF[2])) * 9 + (int(CPF[3])) * 8 + (int(CPF[4])) * 7 + (int(CPF[5])) * 6 + (int(CPF[6])) * 5 + (int(CPF[7])) * 4 + (int(CPF[8])) * 3 + Digito1 * 2

Digito2 = 11 - (Soma2 % 11)

sequencia =  CPF[:-2] == str(CPF[0]*(len(CPF)-2))

if Digito1 == int(CPF[-2]) and Digito2 == int(CPF[-1]) and not sequencia:
    print('CPF Válido.')
else:
    print('CPF Inválido.')



    print("""
    ###########################################################################
    """)


while True:
    # cpf = '16899535009'
    cpf = input('Digite um CPF: ')
    novo_cpf = cpf[:-2]                 # Elimina os dois últimos digitos do CPF
    reverso = 10                        # Contador reverso
    total = 0

    # Loop do CPF
    for index in range(19):
        if index > 8:                   # Primeiro índice vai de 0 a 9,
            index -= 9                  # São os 9 primeiros digitos do CPF

        total += int(novo_cpf[index]) * reverso  # Valor total da multiplicação

        reverso -= 1                    # Decrementa o contador reverso
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:                   # Se o digito for > que 9 o valor é 0
                d = 0
            total = 0                   # Zera o total
            novo_cpf += str(d)          # Concatena o digito gerado no novo cpf

    # Evita sequencias. Ex.: 11111111111, 00000000000...
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    # Descobri que sequências avaliavam como verdadeiro, então também
    # adicionei essa checagem aqui
    if cpf == novo_cpf and not sequencia:
        print('Válido')
    else:
        print('Inválido')