from Formating.GesturesCode.Code import Code


class CodeBuilder:
    def build_click_code(self) -> str:
        return Code.get_code(False, False, False)

    def build_double_click_code(self) -> str:
        return Code.get_code(True, False, False)

    def build_press_code(self) -> str:
        return Code.get_code(True, True, False)

    def build_right_click_code(self) -> str:
        return Code.get_code(True, False, True)

    def build_middle_click_code(self) -> str:
        return Code.get_code(True, True, True)

    def build_game_press_code(self) -> str:
        return self.build_double_click_code()

    def build_game_right_click_code(self) -> str:
        return self.build_press_code()

    def build_game_middle_click_code(self) -> str:
        return self.build_right_click_code()

    def build_game_stop_control_code(self) -> str:
        return self.build_middle_click_code()
