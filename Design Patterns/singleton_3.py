# class Meta(type):
#     def __call__(cls, *args, **kwargs):
#         print('Em metaclasses, CALL é executado primeiro')
#         return super().__call__(*args, **kwargs)

# class Pessoa(metaclass=Meta):
#     def __new__(cls, *args, **kwagrs):
#         print("NEW é executado primeiro")
#         return super().__new__(cls)
    
#     def __init__(self, nome):
#         print("INIT é executado segundo")
#         self.nome = nome

#     def __call__(self, x, y):
#         print('Call chamado', self.nome, x + y)

# p1 = Pessoa('Vinicius')
# print(p1.nome)


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls] 
    

class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = "escuro"
        self.font = '18px'

if __name__ == "__main__":
    as1 = AppSettings()
    as1.tema = 'O tema claro'
    as2 = AppSettings()
    as3 = AppSettings()

    print(as1 == as3)
    print(as1 == as2)
    print(as3 == as2)
