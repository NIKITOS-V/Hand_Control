from typing import Final


class HandPointData:
    def __init__(self, id: int, x: int, y: int):
        self.__id: Final[int] = id
        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_id(self) -> int:
        return self.__id

    def set_x(self, x: int):
        self.__x = x

    def set_y(self, y: int):
        self.__y = y

    def set_coord(self, x: int, y: int):
        self.__x = x
        self.__y = y

    def get_coord(self) -> list[int]:
        return [self.__x, self.__y]
