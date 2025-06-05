from typing import Final


class Value:
    def __init__(
            self,
            max_distance: int,
            activate_distance: int
    ):
        self.__max_distance: Final[int] = max_distance
        self.__activate_distance: Final[int] = activate_distance

    def get_max_distance(self) -> int:
        return self.__max_distance

    def get_activate_distance(self) -> int:
        return self.__activate_distance


class ClickValues(Value):
    def __init__(self):
        super().__init__(150, 50)


class DoubleClickValues(Value):
    def __init__(self):
        super().__init__(260, 240)


class PressValues(Value):
    def __init__(self):
        super().__init__(240, 220)


class KeyValue:
    def __init__(self):
        self.__value: Final[int] = 140

    def get_value(self) -> int:
        return self.__value
