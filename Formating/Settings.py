from typing import Final


class Settings:
    def __init__(
            self,
            id_first_point: int,
            id_second_point: int,
            activate_distance: int
    ):
        self.__id_first_point: Final[int] = id_first_point
        self.__id_second_point: Final[int] = id_second_point
        self.__activate_distance: int = activate_distance

    def get_activate_distance(self) -> int:
        return self.__activate_distance

    def get_id_first_point(self) -> int:
        return self.__id_first_point

    def get_id_second_point(self) -> int:
        return self.__id_second_point