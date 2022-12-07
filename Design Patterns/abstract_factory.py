from abc import ABC, abstractmethod

class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente() -> None: pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente() -> None: pass


class CarroLuxoZN(VeiculoLuxo):
    def buscar_cliente() -> None:
        print('Carro de luxo ZN buscando cliente...')


class  CarroPopularZN(VeiculoPopular):
    def buscar_cliente() -> None:
        print('Carro popular ZN buscando cliente...')


class  MotoZN(VeiculoLuxo):
    def buscar_cliente() -> None:
        print('Moto ZN buscando cliente...')


class  MotoLuxoZN(VeiculoPopular):
    def buscar_cliente() -> None:
        print('Moto de luxo ZN buscando cliente...')


class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente() -> None:
        print('Carro de luxo ZS buscando cliente...')


class  CarroPopularZS(VeiculoPopular):
    def buscar_cliente() -> None:
        print('Carro popular ZS buscando cliente...')


class  MotoZS(VeiculoLuxo):
    def buscar_cliente() -> None:
        print('Moto ZS buscando cliente...')


class  MotoLuxoZS(VeiculoPopular):
    def buscar_cliente() -> None:
        print('Moto de luxo ZS buscando cliente...')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_luxo () -> VeiculoLuxo: pass
    @staticmethod
    @abstractmethod
    def get_carro_popular () -> VeiculoPopular: pass
    @staticmethod
    @abstractmethod    
    def get_moto_luxo () -> VeiculoLuxo: pass
    @staticmethod
    @abstractmethod    
    def get_moto_popular () -> VeiculoPopular: pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo () -> VeiculoLuxo:
        return CarroLuxoZN

    @staticmethod
    def get_carro_popular () -> VeiculoPopular: 
        return CarroPopularZN

    @staticmethod 
    def get_moto_luxo () -> VeiculoLuxo: 
        return MotoLuxoZN

    @staticmethod
    def get_moto_popular () -> VeiculoPopular: 
        return MotoZN

class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_luxo () -> VeiculoLuxo:
        return CarroLuxoZS

    @staticmethod
    def get_carro_popular () -> VeiculoPopular: 
        return CarroPopularZS

    @staticmethod 
    def get_moto_luxo () -> VeiculoLuxo: 
        return MotoLuxoZS

    @staticmethod
    def get_moto_popular () -> VeiculoPopular: 
        return MotoZS


class Cliente:
    def busca_clientes_zn(self):
        for factory in [ZonaNorteVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()

    def busca_clientes_zs(self):
        for factory in  [ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()

            moto_popular = factory.get_moto_popular()
            moto_popular.buscar_cliente()

            moto_luxo = factory.get_moto_luxo()
            moto_luxo.buscar_cliente()


if __name__ == "__main__":
    cliente = Cliente()
    cliente.busca_clientes_zn()
    print()
    cliente.busca_clientes_zs()