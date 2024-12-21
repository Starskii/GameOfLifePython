
class Cell:
    def __init__(self, chunk_position_x: int, chunk_position_y: int):
        self.is_alive = False
        self.is_alive_next = False
        self.chunk_position_x = chunk_position_x
        self.chunk_position_y = chunk_position_y
