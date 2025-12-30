# Defines how the food interacts/behaves in the game
import pygame, random

class Food:
    def __init__(self, game_window):
        self.gw_food = game_window
        self.position = (0, 0)
        self.colorRed = game_window.red
        self.colorBlack = game_window.black
        self.randomize_position()

    def randomize_position(self):
        gw_randomPos = self.gw_food
        self.position = (random.randint(0, gw_randomPos.GRID_WIDTH - 1) * gw_randomPos.GRID_SIZE, random.randint(0, gw_randomPos.GRID_HEIGHT - 1) * gw_randomPos.GRID_SIZE)

    def draw(self, surface):
        gw_draw = self.gw_food
        rect = pygame.Rect((self.position[0], self.position[1]), (gw_draw.GRID_SIZE, gw_draw.GRID_SIZE))
        pygame.draw.rect(surface, self.colorRed, rect)
        pygame.draw.rect(surface, self.colorBlack, rect, 1)