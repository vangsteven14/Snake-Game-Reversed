# Game window setup and configurations
import pygame, sys

class GameWindow:
    def __init__(self):
        # Snake Window Setup
        self.WIDTH = 960
        self.HEIGHT = 960
        self.GRID_SIZE = 40
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), 0, 32)
        self.RESTART = True
        self.MAIN_MENU = True

        self.UI_HEIGHT = 80
        self.GAME_HEIGHT = self.HEIGHT - self.UI_HEIGHT
        self.game_surface = pygame.Surface((self.WIDTH, self.GAME_HEIGHT)).convert()
        self.ui_surface = pygame.Surface((self.WIDTH, self.UI_HEIGHT)).convert()
        self.GRID_HEIGHT = self.GAME_HEIGHT // self.GRID_SIZE
        self.GRID_WIDTH = self.WIDTH // self.GRID_SIZE

        # Snake Window Color Palette
        self.blackBackground = (0, 0, 0)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # Snake Window Directions
        self.UP = (0, -1)
        self.DOWN = (0, 1)
        self.LEFT = (-1, 0)
        self.RIGHT = (1, 0)

        # Snake Score Font & Size
        self.font = pygame.font.Font("freesansbold.ttf", 30)
        self.score = 100

    def drawGrid(self):
        self.game_surface.fill(self.blackBackground)

        for y in range(0, int(self.GRID_HEIGHT)):
            for x in range(0, int(self.GRID_WIDTH)):
                if ((x + y) % 2) == 0:
                    rect1 = pygame.Rect((x * self.GRID_SIZE, y * self.GRID_SIZE), (self.GRID_SIZE, self.GRID_SIZE))
                    pygame.draw.rect(self.game_surface, self.blackBackground, rect1)
                else:
                    rect2 = pygame.Rect((x * self.GRID_SIZE, y * self.GRID_SIZE), (self.GRID_SIZE, self.GRID_SIZE))
                    pygame.draw.rect(self.game_surface, self.blackBackground, rect2)

    def score_display(self):
        self.ui_surface.fill(self.blackBackground)
        text = self.font.render("Food Remaining: {0}".format(self.score), True, self.white)
        text_rect = text.get_rect(midleft=(20, self.UI_HEIGHT // 2))
        self.screen.blit(text, text_rect)

        pygame.draw.rect(
            self.ui_surface,
            self.white,
            pygame.Rect(0, 0, self.WIDTH, self.UI_HEIGHT),
            3
        )

    def main_menu(self):
        while self.MAIN_MENU:
            self.screen.fill(self.blackBackground)
            self.lines = [
                "Welcome",
                "to",
                "Snake Game: Reversed!",
                "",
                "Press ENTER to START or ESC to Exit"
            ]    
            start_y = self.HEIGHT // 2 - 200

            for i, self.lines in enumerate(self.lines):
                menu_text = self.font.render(self.lines, True, self.white)
                menu_box = menu_text.get_rect(center=(self.WIDTH // 2, start_y + i * 50))
                self.screen.blit(menu_text, menu_box) 

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.MAIN_MENU = False