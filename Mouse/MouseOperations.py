import win32api, win32con
import mouse


class MouseOperations:
    def __init__(self):
        self.__clicked: bool = False
        self.__double_clicked: bool = False
        self.__pressed: bool = False
        self.__right_clicked: bool = False
        self.__middle_clicked: bool = False

    def move(self, x: int, y: int) -> None:
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)

    def set_pos(self, x: int, y: int) -> None:
        win32api.SetCursorPos((x, y))

    def get_pos(self) -> list[int]:
        return mouse.get_position()

    def click(self, activate: bool) -> None:
        if not activate:

            if self.__clicked:
                self.__clicked = False

        elif not self.__clicked:
            x, y = mouse.get_position()

            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x, y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

            self.__clicked = True

    def double_click(self, activate: bool) -> None:
        if not activate:

            if self.__double_clicked:
                self.__double_clicked = False

        elif not self.__double_clicked:
            x, y = mouse.get_position()

            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

            self.__double_clicked = True

    def press(self, activate: bool) -> None:
        if not activate:

            if self.__pressed:
                x, y = mouse.get_position()

                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

                self.__pressed = False

        elif not self.__pressed:
            x, y = mouse.get_position()

            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)

            self.__pressed = True

    def right_click(self, activate: bool) -> None:
        if not activate:

            if self.__right_clicked:
                self.__right_clicked = False

        elif not self.__right_clicked:
            x, y = mouse.get_position()

            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)

            self.__right_clicked = True

    def middle_click(self, activate: bool) -> None:
        if not activate:

            if self.__middle_clicked:
                self.__middle_clicked = False

        elif not self.__middle_clicked:
            x, y = mouse.get_position()

            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, x, y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, x, y, 0, 0)

            self.__middle_clicked = True
