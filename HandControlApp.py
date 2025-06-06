import ctypes
from typing import Final
import cv2
import mediapipe as mp
import keyboard
import time

from Formating.Hand.HandData import HandData
from Mouse.MouseController import MouseController


class HandControlApp:
    def __init__(
            self,
            hand_data: HandData,
            mouse_controller: MouseController,
            esc_key: str = "o",
            pause_key: str = "p",
            daily_mode_key: str = "i",
            game_mode_key: str = "u"
    ):
        self.__hand_data: HandData = hand_data
        self.__mouse_controller: MouseController = mouse_controller

        self.__hands = mp.solutions.hands.Hands()

        self.__run_app: bool = True
        self.__hand_vision: bool = True

        keyboard.add_hotkey(esc_key, self.__stop_app)
        keyboard.add_hotkey(pause_key, self.__start_and_stop_vision)
        keyboard.add_hotkey(daily_mode_key, self.__mouse_controller.start_daily_mode)
        keyboard.add_hotkey(game_mode_key, self.__mouse_controller.start_game_mode)

    def mainloop(self) -> None:
        cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
        monitor_size: Final[list[int]] = self.__calc_monitor_size()
        flip_code: Final[int] = 1

        while self.__run_app:
            while self.__hand_vision and self.__run_app:
                self.__update_hand_data(
                    cv2.flip(
                        cap.read()[1],
                        flip_code
                    ),
                    monitor_size
                )

                self.__mouse_controller.check_mouse()

            time.sleep(0.1)

    def __start_and_stop_vision(self) -> None:
        self.__hand_vision = not self.__hand_vision

    def __stop_app(self) -> None:
        self.__run_app = False

    def __calc_monitor_size(self) -> list[int]:
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        return [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

    def __calc_normal_coord(self, monitor_side: int, lm_coord) -> int:
        return int(round(monitor_side * lm_coord))

    def __update_hand_data(self, image, monitor_size: list[int]) -> None:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.__hands.process(gray_image)

        if results.multi_hand_landmarks:

            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):

                    self.__hand_data.get_data(id).set_coord(
                        self.__calc_normal_coord(monitor_size[0], lm.x),
                        self.__calc_normal_coord(monitor_size[1], lm.y)
                    )

            self.__mouse_controller.hand_found()

        else:
            self.__mouse_controller.hand_lost()
