from Cell import Cell

class Chunk:
    def __init__(self, chunk_size: int, up_chunk = None, down_chunk = None, left_chunk = None, right_chunk = None):
        self.grid = [[Cell(x, y) for x in range(chunk_size)] for y in range(chunk_size)]

    def check_living(self, x, y):
        if x < 0 or x >= len(self.grid) or y < 0 or y >= len(self.grid):
            # Outside bounds of chunk
            # TODO add dynamic chunk growth here
            return False
        return self.grid[x][y].is_alive

    def calculate_next_state(self, x_grid_position, y_grid_position):
        living_count = 0
        for y_modifier_grid_position in range(-1, 2):
            for x_modifier_grid_position in range(-1, 2):
                if x_modifier_grid_position == 0 and y_modifier_grid_position == 0:
                    continue
                if self.check_living(x_grid_position + x_modifier_grid_position, y_grid_position + y_modifier_grid_position):
                    living_count += 1
        if self.grid[x_grid_position][y_grid_position].is_alive:
            return 1 < living_count < 4
        else:
            return living_count == 3


    def calculate_next_generation(self):
        for y_grid_position in range(0, len(self.grid)):
            for x_grid_position in range(0, len(self.grid)):
                self.grid[x_grid_position][y_grid_position].is_alive_next = self.calculate_next_state(x_grid_position, y_grid_position)

    def advance_to_next_generation(self):
        for y_grid_position in range(0, len(self.grid)):
            for x_grid_position in range(0, len(self.grid)):
                self.grid[x_grid_position][y_grid_position].is_alive = self.grid[x_grid_position][y_grid_position].is_alive_next