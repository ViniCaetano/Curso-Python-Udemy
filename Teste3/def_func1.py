def func1 ():
    return 'Isso é uma função.'

def func2 (funcao):
    return funcao()

print(func2(func1))