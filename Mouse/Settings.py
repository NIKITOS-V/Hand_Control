from typing import Final

from Formating.Settings import Settings


class MoveSettings:
    def __init__(self):
        self.__id_moving_point: Final[int] = 8
        self.__id_spawn_point: Final[int] = 5

    def get_id_moving_point(self) -> int:
        return self.__id_moving_point

    def get_id_spawn_point(self) -> int:
        return self.__id_spawn_point


class NormalValue:
    def __init__(self):
        self.__value: Final[int] = 140
        self.__id_first_point: Final[int] = 0
        self.__id_second_point: Final[int] = 9

    def get_value(self) -> int:
        return self.__value

    def get_id_first_point(self) -> int:
        return self.__id_first_point

    def get_id_second_point(self) -> int:
        return self.__id_second_point


class ActivateSettings(Settings):
    def __init__(self):
        super().__init__(5, 4, 70)


class DoubleClickSettings(Settings):
    def __init__(self):
        super().__init__(0, 12, 260)


class PressSettings(Settings):
    def __init__(self):
        super().__init__(12, 8, 60)


class RightClickSettings(Settings):
    def __init__(self):
        super().__init__(0, 16, 220)


