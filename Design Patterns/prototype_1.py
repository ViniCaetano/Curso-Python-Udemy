from __future__ import annotations
from typing import List
from copy import deepcopy

class StringReprMixing:
    def __str__(self):
        params = ', '.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Person(StringReprMixing):
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

class Address(StringReprMixing):
    def __init__(self, street: str, number: str) -> None:
        self.street = street
        self.number = number


if __name__ == '__main__':
    vinicius = Person('Vinicius', 'Caetano')
    endereco_vinicius = Address('R1', '1000')
    vinicius.add_address(endereco_vinicius)

    esposa_vinicius = deepcopy(vinicius)
    esposa_vinicius.firstname = 'Isabela'
    
    
    print(vinicius)
    print(esposa_vinicius)