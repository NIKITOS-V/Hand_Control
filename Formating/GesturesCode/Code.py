class Code:

    @classmethod
    def get_code(
            self,
            thumb: bool,
            thumb_and_index_finger: bool,
            ring_finger: bool
    ) -> str:
        return (
            f"{int(thumb)}"
            f"{int(thumb_and_index_finger)}"
            f"{int(ring_finger)}"
        )
