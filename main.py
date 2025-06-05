from Formating.HandData import HandData
from HandControlApp import HandControlApp
from MouseController import MouseController

if __name__ == "__main__":
    hand_data: HandData = HandData()

    mouse_controller: MouseController = MouseController(
        hand_data
    )

    HandControlApp(
        hand_data,
        mouse_controller
    ).mainloop()
