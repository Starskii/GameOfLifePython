import pygame
import sys
import time

class View:
    def __init__(self, chunk):
        self.play_flag = False
        self.time_start = None
        self.time_interval = .1
        self.chunk = chunk
        self.BLACK = (0, 0, 0)
        self.WHITE = (200, 200, 200)
        self.RED = (200, 40, 40)
        self.BLUE = (40, 40, 200)
        self.WINDOW_HEIGHT = 1000
        self.WINDOW_WIDTH = 1000
        self.block_size_px = int(self.WINDOW_HEIGHT / len(chunk.grid))  # Set the size of the grid block
        global SCREEN, CLOCK
        pygame.init()
        SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        CLOCK = pygame.time.Clock()
        SCREEN.fill(self.BLACK)

        while True:
            self.drawGrid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    cell_index_x = int(pos[0]/self.block_size_px)
                    cell_index_y = int(pos[1]/self.block_size_px)
                    chunk.grid[cell_index_x][cell_index_y].is_alive = not chunk.grid[cell_index_x][cell_index_y].is_alive
                if event.type == pygame.MOUSEBUTTONUP and event.button == 2:
                    self.play_flag = not self.play_flag
                    self.time_start = time.time()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    chunk.calculate_next_generation()
                    chunk.advance_to_next_generation()
            if self.play_flag and time.time() - self.time_start > self.time_interval:
                chunk.calculate_next_generation()
                chunk.advance_to_next_generation()
                self.time_start = time.time()


            pygame.display.update()

    def drawGrid(self):
        for x in range(0, self.WINDOW_WIDTH, self.block_size_px):
            for y in range(0, self.WINDOW_HEIGHT, self.block_size_px):
                rect = pygame.Rect(x, y, self.block_size_px, self.block_size_px)
                color = self.WHITE
                border_color = self.BLACK
                cell_index_x = int(x / self.block_size_px)
                cell_index_y = int(y / self.block_size_px)
                if self.chunk.grid[cell_index_x][cell_index_y].is_alive:
                    color = self.BLACK
                    border_color = self.WHITE
                pygame.draw.rect(SCREEN, color, rect)
                pygame.draw.rect(SCREEN, border_color, rect, 1)
