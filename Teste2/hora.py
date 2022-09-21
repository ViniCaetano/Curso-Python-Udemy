hora = input('Que horas são? 0-23: ')
if hora.isnumeric():
    hora = int(hora)
    if hora >= 0 and hora < 12:
        print('Bom dia! 0-11')
    elif hora >= 12 and hora < 18:
        print('Boa tarde! 12-17')
    elif hora >= 18 and hora < 24:
        print('Boa noite! 18-23')
    else:
        print('Digite horas válidas. 0-23')
else:
    print('Digite horas válidas. 0-23')