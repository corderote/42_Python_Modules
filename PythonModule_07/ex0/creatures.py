from abc import ABC, abstractmethod


class Creature(ABC):

    _name: str = ""
    _type: list[str] = []
    _attacks: list[str] = []

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        type_str = "/".join(self._type)
        return f"{self._name} is a {type_str} Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        self._name = "Flameling"
        self._type = ["Fire"]
        self._attacks = ["Ember"]
        super().__init__()

    def attack(self) -> str:
        return f"{self._name} uses {self._attacks[0]}!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        self._name = "Pyrodon"
        self._type = ["Fire", "Flying"]
        self._attacks = ["Flamethrower"]
        super().__init__()

    def attack(self) -> str:
        return f"{self._name} uses {self._attacks[0]}!"


class Aquabub(Creature):
    def __init__(self) -> None:
        self._name = "Aquabub"
        self._type = ["Water"]
        self._attacks = ["Water Gun"]
        super().__init__()

    def attack(self) -> str:
        return f"{self._name} uses {self._attacks[0]}!"


class Torragon(Creature):
    def __init__(self) -> None:
        self._name = "Torragon"
        self._type = ["Water"]
        self._attacks = ["Hydro Pump"]
        super().__init__()

    def attack(self) -> str:
        return f"{self._name} uses {self._attacks[0]}!"
