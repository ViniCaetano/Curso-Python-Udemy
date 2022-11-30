def Soma(x, y):
    """Soma x e y

    >>> Soma(10, 20)
    30
    
    >>> Soma(-10, 20)
    10

    >>> Soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: X precisa ser INT ou FLOAT
    """
    assert isinstance(x, (int, float)), "X precisa ser INT ou FLOAT"
    assert isinstance(y, (int, float)), "Y precisa ser INT ou FLOAT"
    return x + y


def Subtrai(x, y):
    """Subtrai x e y
    
    >>> Subtrai(10, 5)
    5

    >>> Subtrai('10', 5)
    5
    """
    
    assert isinstance(x, (int, float)), "X precisa ser INT ou FLOAT"
    assert isinstance(y, (int, float)), "Y precisa ser INT ou FLOAT"
    return x-y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)