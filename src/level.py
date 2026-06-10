from abc import abstractmethod, ABC





class Level(ABC):

    def __init__(self) -> None:
        self.time_limit = 90
        pass

    @abstractmethod
    def time_reached() -> None:
        pass


class Level1(Level):


    def __init__(self) -> None:
        pass


class Level2(Level):


    def __init__(self) -> None:
        self.time_limit = 120


    def time_reached(self) -> None:
        pass


class Level3(Level):

    def __init__(self) -> None:
        self.time_limit = 120

