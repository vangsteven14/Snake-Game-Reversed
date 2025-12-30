# The classic Snake game but reversed!
# Main file to run the Fat Snake game
import pygame, sys
from game_window import GameWindow
from snake import Snake
from food import Food

pygame.display.set_caption("Snake Game: Reversed!")
pygame.init()

class FatSnake(GameWindow, Snake, Food):
    def run_snake_reversed(self):
        pygame.init()
        snake_window = GameWindow()
        snake_object = Snake(snake_window)
        snake_food = Food(snake_window)
        paused = False

        while True:
            snake_window.main_menu()
            self.clock.tick(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_SPACE:
                        paused = not paused
                    else:
                        snake_object.handle_keys(event.key)
            
            snake_window.drawGrid()
            
            if not paused:
                snake_object.move()

                if snake_object.get_head_position() == snake_food.position:
                    if snake_object.length > 0:
                        snake_object.length -= 1
                        snake_window.score -= 1
                        snake_food.randomize_position()
                        snake_object.positions.pop()

            snake_object.draw(snake_window.game_surface)
            snake_food.draw(snake_window.game_surface)

            snake_window.screen.blit(snake_window.ui_surface, (0, 0))
            snake_window.screen.blit(snake_window.game_surface, (0, snake_window.UI_HEIGHT))
            snake_window.score_display()

            if paused:
                paused_text1 = snake_window.font.render("Game Paused.", True, snake_window.white)
                paused_text2 = snake_window.font.render("Press SPACE to Resume.", True, snake_window.white)

                paused_box1 = paused_text1.get_rect(center=(snake_window.WIDTH // 2, snake_window.HEIGHT // 2 + 25 - 100))
                paused_box2 = paused_text2.get_rect(center=(snake_window.WIDTH // 2, snake_window.HEIGHT // 2 + 75 - 100))

                paused_padding = 12

                outline_rect1 = paused_box1.inflate(paused_padding * 2, paused_padding * 2)
                outline_rect2 = paused_box2.inflate(paused_padding * 2, paused_padding * 2)

                outline_rect_full = outline_rect1.union(outline_rect2)

                pygame.draw.rect(snake_window.screen, snake_window.white, outline_rect_full, 2)

                snake_window.screen.blit(paused_text1, paused_box1)
                snake_window.screen.blit(paused_text2, paused_box2)

            if snake_window.score == 0:
                    win1 = snake_window.font.render("You've Won!", True, snake_window.white)
                    win2 = snake_window.font.render("Press R to Restart or ESC/Close Window to Exit", True, snake_window.white)
                    snake_window.screen.fill(snake_window.blackBackground)
                    win1_box = win1.get_rect(center=(snake_window.WIDTH // 2, snake_window.HEIGHT // 2 + 25 - 100))
                    win2_box = win2.get_rect(center=(snake_window.WIDTH // 2,
                    snake_window.HEIGHT // 2 + 75 - 100))
                    snake_window.screen.blit(win1, win1_box)
                    snake_window.screen.blit(win2, win2_box)
                    pygame.display.update()

                    while snake_window.RESTART:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                                snake_object.reset()
                                snake_window.score = 100
                                snake_food.randomize_position()
                                snake_window.RESTART = False

            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            continue

def main():
    fat_snake = FatSnake()
    fat_snake.run_snake_reversed()

if __name__ == "__main__":
    main()