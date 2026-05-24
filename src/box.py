

class Box:

    def __init__(self, type_box: int) -> None:
        """Init box."""
        self.type_box = type_box
        self.pacgum: bool = False
        self.super_pacgum: bool = False