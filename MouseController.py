from Formating.HandData import HandData
from Formating.HandPointData import HandPointData
from NormalValues import *

from math import sqrt
import mouse
import keyboard


class MouseController:
    def __init__(self, hand_data: HandData):
        self.__hand_data: HandData = hand_data

        self.click_values: ClickValues = ClickValues()
        self.double_click_values: DoubleClickValues = DoubleClickValues()
        self.press_values: PressValues = PressValues()
        self.key_value: KeyValue = KeyValue()

        self.__hand_is_visible: bool = False

        self.__hand_is_found: bool = False

        self.__old_mouse_pos: list[int] = [0, 0]

        self.__sensitivity: Final[float] = 2

    def hand_lost(self) -> None:
        self.__hand_is_visible = False
        self.__hand_is_found = False

    def hand_found(self) -> None:
        if not self.__hand_is_found:
            self.__hand_is_visible = True

            x, y = self.__hand_data.get_data(8).get_coord()

            mouse.move(x, y)

            self.__old_mouse_pos[0] = x
            self.__old_mouse_pos[1] = y

            self.__hand_is_found = True

    def check_mouse(self) -> None:
        if self.__hand_is_visible:
            self.__move_mouse()

    def __move_mouse(self) -> None:
        x, y = self.__hand_data.get_data(8).get_coord()

        mouse.move(
            self.__calc_normal_moving_distance(x - self.__old_mouse_pos[0]),
            self.__calc_normal_moving_distance(y - self.__old_mouse_pos[1]),
            absolute=False
        )

        self.__old_mouse_pos[0] = x
        self.__old_mouse_pos[1] = y

    def __calc_normal_moving_distance(self, distance: int) -> int:
        return int(round(self.__sensitivity * distance))

    def __calc_normal_vector_len(self, hand_point_1: HandPointData, hand_point_2: HandPointData) -> int:
        return int(round(self.__calc_vector_len(hand_point_1, hand_point_2) * self.__calc_ratio()))

    def __calc_vector_len(self, hand_point_1: HandPointData, hand_point_2: HandPointData) -> float:
        return sqrt(
                (hand_point_1.get_x() - hand_point_2.get_x())**2 +
                (hand_point_1.get_y() - hand_point_2.get_y())**2
            )

    def __calc_ratio(self) -> float:
        return self.key_value.get_value() / self.__calc_vector_len(
                self.__hand_data.get_data(0), self.__hand_data.get_data(9)
            )