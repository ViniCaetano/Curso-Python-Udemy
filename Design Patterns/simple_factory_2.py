from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass

class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo buscando cliente...')

class  CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular buscando cliente...')

class  Moto(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto buscando cliente...')

class  MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto de luxo buscando cliente...')

class VeiculoFactory:
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)
    
    @staticmethod
    def get_carro (tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        if tipo == 'moto':
            return Moto()   
        if tipo == 'moto de luxo':
            return MotoLuxo()
        assert 0, 'Veículo não existe'
    
    def buscar_cliente(self):
        self.carro.buscar_cliente()


if __name__ == "__main__":
    from random import choice
    carros_disponiveis = ['luxo', 'popular', 'moto', 'moto de luxo']

    for i in range(10):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente()
