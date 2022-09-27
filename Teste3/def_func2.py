def func1 (arg1, *args, **kwargs):
    return arg1(*args, **kwargs)

def func2 (arg1):
    return f'Olá {arg1}'

def func3 (arg1, arg2):
    return f'{arg1} {arg2}'

print(func1(func2, 'Vinicius'))
print(func1(func3, 'Vinicius', 'Tudo bem?'))