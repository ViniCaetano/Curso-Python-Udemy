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

class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)
    
    @staticmethod
    @abstractmethod
    def get_carro (tipo: str) -> Veiculo: pass
    
    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
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

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro (tipo: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        if tipo == 'popular':
            return CarroPopular()
        assert 0, 'Veículo não existe'


if __name__ == "__main__":
    from random import choice
    veiculos_disponiveis_zona_norte = ['luxo', 'popular', 'moto', 'moto de luxo']
    veiculos_disponiveis_zona_sul = ['luxo', 'popular']    

    print('ZONA NORTE')
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

    print()

    print('ZONA SUL')
    for i in range(10):
        carro2 = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
