import ctypes
from typing import Final
import cv2
import mediapipe as mp
import imutils
import keyboard

from Formating.HandData import HandData
from MouseController import MouseController


class HandControlApp:
    def __init__(
            self,
            hand_data: HandData,
            mouse_controller: MouseController,
            esc_key: str = "esc"
    ):
        self.__hand_data: HandData = hand_data
        self.__mouse_controller: MouseController = mouse_controller

        self.__hands = mp.solutions.hands.Hands()

        self.__run_app: bool = True

        keyboard.add_hotkey(esc_key, self.__stop_app)

    def mainloop(self) -> None:
        cap = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
        monitor_size: Final[list[int]] = self.__calc_monitor_size()
        flip_code: Final[int] = 1

        while self.__run_app:
            self.__update_hand_data(
                cv2.flip(
                    imutils.resize(
                        cap.read()[1],
                        width=monitor_size[0],
                        height=monitor_size[1]
                    ),
                    flip_code
                )
            )

            self.__mouse_controller.check_mouse()

    def __stop_app(self) -> None:
        self.__run_app = False

    def __calc_monitor_size(self) -> list[int]:
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        return [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

    def __update_hand_data(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.__hands.process(gray_image)

        if results.multi_hand_landmarks:

            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):

                    self.__hand_data.get_data(id).set_coord(
                        image.shape[1] * lm.x,
                        image.shape[0] * lm.y
                    )

            self.__mouse_controller.hand_found()

        else:
            self.__mouse_controller.hand_lost()
