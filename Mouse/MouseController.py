from Formating.GesturesCode.Code import Code
from Formating.GesturesCode.CodeBuilder import CodeBuilder
from Formating.Hand.HandData import HandData
from Formating.Hand.HandPointData import HandPointData
from Mouse.MouseOperations import MouseOperations
from Mouse.Settings import *

from math import sqrt


class MouseController:
    def __init__(self, hand_data: HandData):
        self.__hand_data: HandData = hand_data

        self.__move_settings: MoveSettings = MoveSettings()
        self.__press_settings: PressSettings = PressSettings()
        self.__normal_value: NormalValue = NormalValue()
        self.__activate_settings: ActivateSettings = ActivateSettings()
        self.__double_click_settings: DoubleClickSettings = DoubleClickSettings()
        self.__right_click_settings: RightClickSettings = RightClickSettings()

        self.__mouse_operations: MouseOperations = MouseOperations()

        self.__hand_is_visible: bool = False
        self.__hand_is_found: bool = False

        self.__old_mouse_pos: list[int] = [0, 0]

        self.__sensitivity: Final[float] = 2
        self.__stab_ration: Final[float] = 0.5
        self.__monitor_scale: Final[float] = 1.25

        self.__code_builder: CodeBuilder = CodeBuilder()

        self.__daily_operations: Final[dict] = {
            self.__code_builder.build_click_code(): self.__mouse_operations.click,
            self.__code_builder.build_double_click_code(): self.__mouse_operations.double_click,
            self.__code_builder.build_press_code(): self.__mouse_operations.press,
            self.__code_builder.build_right_click_code(): self.__mouse_operations.right_click,
            self.__code_builder.build_middle_click_code(): self.__mouse_operations.middle_click
        }

        self.__game_operations: Final[dict] = {
            self.__code_builder.build_click_code(): self.__mouse_operations.click,
            self.__code_builder.build_game_press_code(): self.__mouse_operations.press,
            self.__code_builder.build_game_right_click_code(): self.__mouse_operations.right_click,
            self.__code_builder.build_game_middle_click_code(): self.__mouse_operations.middle_click
        }

        self.check_mouse = self.__daily_check_mouse

    def hand_lost(self) -> None:
        self.__hand_is_visible = False
        self.__hand_is_found = False

    def hand_found(self) -> None:
        if not self.__hand_is_found:

            self.__hand_is_visible = True
            self.__hand_is_found = True

            self.__move_mouse()

    def __get_move_point(self) -> HandPointData:
        return self.__hand_data.get_data(self.__move_settings.get_id_moving_point())

    def __get_spawn_point(self) -> HandPointData:
        return self.__hand_data.get_data(self.__move_settings.get_id_spawn_point())

    def start_game_mode(self) -> None:
        self.check_mouse = self.__game_check_mouse

    def start_daily_mode(self) -> None:
        self.check_mouse = self.__daily_check_mouse

    def __daily_check_mouse(self) -> None:
        if self.__hand_is_visible:

            self.__move_mouse()

            try:
                self.__daily_operations[
                    Code.get_code(
                        self.__is_thumb(),
                        self.__is_thumb_and_index_finger(),
                        self.__is_ring_finger()
                    )
                ](
                    self.__is_activate()
                )

            except KeyError:
                pass

    def __game_check_mouse(self) -> None:
        if self.__hand_is_visible:

            code: str = Code.get_code(
                self.__is_thumb(),
                self.__is_thumb_and_index_finger(),
                self.__is_ring_finger()
            )

            if code != self.__code_builder.build_game_stop_control_code():
                self.__move_mouse()

            else:
                self.__update_old_mouse_pos(
                    self.__get_move_point().get_x(),
                    self.__get_move_point().get_y()
                )

            try:
                self.__game_operations[code](
                    self.__is_activate()
                )

            except KeyError:
                pass

    def __move_mouse(self) -> None:
        x: int = self.__calc_uncorrected_coord(self.__get_move_point().get_x())
        y: int = self.__calc_uncorrected_coord(self.__get_move_point().get_y())

        print(self.__get_move_point().get_coord())

        self.__mouse_operations.move(
            self.__calc_normal_moving_distance(
                self.__mouse_operations.get_pos()[0],
                self.__calc_stab_coord(self.__old_mouse_pos[0], x)
            ),
            self.__calc_normal_moving_distance(
                self.__mouse_operations.get_pos()[1],
                self.__calc_stab_coord(self.__old_mouse_pos[1], y)
            )
        )

        self.__update_old_mouse_pos(x, y)

    def __is_thumb_and_index_finger(self) -> bool:
        return self.__calc_normal_vector_len(
            self.__hand_data.get_data(self.__press_settings.get_id_first_point()),
            self.__hand_data.get_data(self.__press_settings.get_id_second_point())
        ) > self.__press_settings.get_activate_distance() and self.__is_thumb()

    def __is_ring_finger(self) -> bool:
        return self.__calc_normal_vector_len(
            self.__hand_data.get_data(self.__right_click_settings.get_id_first_point()),
            self.__hand_data.get_data(self.__right_click_settings.get_id_second_point())
        ) > self.__right_click_settings.get_activate_distance()

    def __is_thumb(self) -> bool:
        return self.__calc_normal_vector_len(
            self.__hand_data.get_data(self.__double_click_settings.get_id_first_point()),
            self.__hand_data.get_data(self.__double_click_settings.get_id_second_point())
        ) > self.__double_click_settings.get_activate_distance()

    def __is_activate(self) -> bool:
        return self.__calc_normal_vector_len(
            self.__hand_data.get_data(self.__activate_settings.get_id_first_point()),
            self.__hand_data.get_data(self.__activate_settings.get_id_second_point())
        ) < self.__activate_settings.get_activate_distance()

    def __update_old_mouse_pos(self, x: int, y: int) -> None:
        self.__old_mouse_pos[0] = x
        self.__old_mouse_pos[1] = y

    def __calc_normal_moving_distance(self, curr_coord: int, stab_coord: int) -> int:
        return self.__round_int(
            (stab_coord - curr_coord) * self.__calc_scale_ratio() * self.__sensitivity / self.__monitor_scale
        )

    def __calc_normal_vector_len(self, hand_point_1: HandPointData, hand_point_2: HandPointData) -> int:
        return int(round(self.__calc_vector_len(hand_point_1, hand_point_2) * self.__calc_scale_ratio()))

    def __calc_vector_len(self, hand_point_1: HandPointData, hand_point_2: HandPointData) -> float:
        return sqrt(
                (hand_point_1.get_x() - hand_point_2.get_x())**2 +
                (hand_point_1.get_y() - hand_point_2.get_y())**2
            )

    def __calc_scale_ratio(self) -> float:
        return self.__normal_value.get_value() / self.__calc_vector_len(
            self.__hand_data.get_data(self.__normal_value.get_id_first_point()),
            self.__hand_data.get_data(self.__normal_value.get_id_second_point())
        )

    def __calc_stab_coord(self, old_coord: int, new_coord: int) -> int:
        return self.__round_int(old_coord + (new_coord - old_coord) * self.__stab_ration)

    def __round_int(self, value) -> int:
        return int(round(value))

    def __calc_corrected_coord(self, coord: int) -> int:
        return self.__round_int(coord / self.__monitor_scale)

    def __calc_uncorrected_coord(self, coord: int) -> int:
        return self.__round_int(coord * self.__monitor_scale)