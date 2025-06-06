from typing import Final

from Formating.Hand.HandPointData import HandPointData


class HandData:
    def __init__(self):
        self.__max_point_number: Final[int] = 21

        self.__point_datas: list[HandPointData] = [
            HandPointData(id, 0, 0) for id in range(self.__max_point_number)
        ]

    def get_data(self, id: int) -> HandPointData:
        return self.__point_datas[id]

    def get_all_data(self) -> list[HandPointData]:
        return self.__point_datas
