# Import pygame module 
import pygame
pygame.init()


# Window Screen Size for Game
Screen_width = 1000
Screen_height = 600
gameWindowSize = pygame.display.set_mode((Screen_width,Screen_height))


# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()


# Initialized exitGame or gameOver = False 
exit_game = False
game_over = False

# Loop for window Screen and Exit button
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True


pygame.quit()
quit()