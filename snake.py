# Defines how the snake interacts/behaves in the game
import pygame, sys, random

class Snake:
    def __init__(self, game_window):
        self.gw_snake = game_window
        self.length = 100
        self.positions = [((game_window.WIDTH / 2), (game_window.HEIGHT / 2))]
        self.direction = random.choice([
            game_window.UP,
            game_window.DOWN,
            game_window.LEFT,
            game_window.RIGHT])
        self.colorGreen = game_window.green
        self.colorBlack = game_window.black
    
    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):    
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else: 
            self.direction = point

    def move(self):
        gw_move = self.gw_snake
        current = self.get_head_position()
        x, y = self.direction
        newPos = (((current[0] + (x * gw_move.GRID_SIZE)) % gw_move.WIDTH), (current[1] + (y * gw_move.GRID_SIZE)) % gw_move.HEIGHT)
        if len(self.positions) > 2 and newPos in self.positions[2:]:
            #self.reset()
            self.game_over()
        else:
            self.positions.insert(0, newPos)
            if len(self.positions) > self.length:
                self.positions.pop()
    
    def reset(self):
        gw_reset = self.gw_snake
        self.length = 100
        gw_reset.score = 100
        self.positions = [((gw_reset.WIDTH / 2), (gw_reset.HEIGHT / 2))]
        self.direction = random.choice([gw_reset.UP, gw_reset.DOWN, gw_reset.LEFT, gw_reset.RIGHT])
    
    def game_over(self):
        gw_game_over = self.gw_snake
        win_text1 = gw_game_over.font.render("Remaining Food: {0}".format(gw_game_over.score), True, gw_game_over.white)
        win_text2 = gw_game_over.font.render("Better Luck Next Time!", True, gw_game_over.white)
        win_text3 = gw_game_over.font.render("Press R to Restart or ESC/Close Window to Exit", True, gw_game_over.white)
        win_text1_box = win_text1.get_rect(center=(gw_game_over.WIDTH // 2, gw_game_over.HEIGHT // 2 - 25 - 100))
        win_text2_box = win_text2.get_rect(center=(gw_game_over.WIDTH // 2, gw_game_over.HEIGHT // 2 + 25 - 100))
        win_text3_box = win_text3.get_rect(center=(gw_game_over.WIDTH // 2, gw_game_over.HEIGHT // 2 + 75 - 100))
        gw_game_over.screen.fill(gw_game_over.blackBackground)
        gw_game_over.screen.blit(win_text1, win_text1_box)
        gw_game_over.screen.blit(win_text2, win_text2_box)
        gw_game_over.screen.blit(win_text3, win_text3_box)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.reset()
                    return

    def draw(self, surface):
        gw_draw = self.gw_snake
        for pos in self.positions:
            rect = pygame.Rect((pos[0], pos[1]), (gw_draw.GRID_SIZE, gw_draw.GRID_SIZE))
            pygame.draw.rect(surface, self.colorGreen, rect)
            pygame.draw.rect(surface, self.colorBlack, rect, 1)

    def handle_keys(self, key):
        gw_handle_keys = self.gw_snake
        
        if key == pygame.K_UP:
            self.turn(gw_handle_keys.UP)
        elif key == pygame.K_DOWN:
            self.turn(gw_handle_keys.DOWN)
        elif key == pygame.K_LEFT:
            self.turn(gw_handle_keys.LEFT)
        elif key == pygame.K_RIGHT:
            self.turn(gw_handle_keys.RIGHT)