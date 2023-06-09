"""
Этот код создает абстрактную фабрику `Creator`, а также два конкретных
создателя `ConcreteCreator1` и `ConcreteCreator2`. Каждый из них возвращает
свой собственный продукт: `ConcreteProduct1` или `ConcreteProduct2`.
"""

from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def do_something(self):
        product = self.factory_method()
        result = (
            f"Creator: The same creator's code has just worked "
            f"with {product.operation()}"
        )

        return result


class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{creator.do_something()}"
    )


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(ConcreteCreator1())

    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(ConcreteCreator2())
