from typing import Final

from Formating.Settings import Settings


class MoveSettings:
    def __init__(self):
        self.__id_moving_point: Final[int] = 8
        self.__id_spawn_point: Final[int] = 9

    def get_id_moving_point(self) -> int:
        return self.__id_moving_point

    def get_id_spawn_point(self) -> int:
        return self.__id_spawn_point


class NormalValue:
    def __init__(self):
        self.__value: Final[int] = 140

    def get_value(self) -> int:
        return self.__value


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


