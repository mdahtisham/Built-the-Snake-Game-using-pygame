# Import pygame module 
import pygame
pygame.init()


# Initialized the Color
white = (255,255,255)
Green = (0,128,0)
Black = (0,0,0)
Red = (255,0,0)


# Window Screen Size for Game
Screen_width = 1000
Screen_height = 600
gameWindowSize = pygame.display.set_mode((Screen_width,Screen_height))


# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()                          # Display Update


# Clock
clock = pygame.time.Clock()


# Initialized exitGame or gameOver = False 
exit_game = False
game_over = False


# Snake Length , Starting Position from X or Y
snk_len = 15
snk_x = 55
snk_y = 55
fps = 30                   # Add fps (Frame per Second)




# Loop for window Screen and Exit button
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True


    # Keys Handling
        if event.type == pygame.KEYDOWN:

        
            #  Right Key
            if event.key == pygame.K_RIGHT:
                # pass
                snk_x = snk_x + 10   # snk_x value is 55 if press the RIGHT ARROW key then snk_x will move right direction +10


             #  Left Key
            if event.key == pygame.K_LEFT:
                # pass
                snk_x = snk_x - 10   # snk_x value is 55 if press the LEFT ARROW key then snk_x will move left direction -10


            # Up Key
            if event.key == pygame.K_UP:
                # pass
                snk_y = snk_y - 10

            # Down Key
            if event.key == pygame.K_DOWN:
                # pass
                snk_y = snk_y + 10


    #  Change the Background WHITE (By Default it is BLACK)
    gameWindowSize.fill(white)

    # Create a Snake with the help rect() function
    pygame.draw.rect(gameWindowSize, Red, [snk_x, snk_y, snk_len, snk_len])

    pygame.display.update()            # Display Update

    # Add fps (Frame per Second)
    clock.tick(fps)


pygame.quit()
quit()