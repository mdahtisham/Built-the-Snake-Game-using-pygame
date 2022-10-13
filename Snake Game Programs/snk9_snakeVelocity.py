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


# Snake Velocity value
vel_x = 0
vel_y = 0



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
                vel_x = 10
                vel_y = 0

            #  Left Key
            if event.key == pygame.K_LEFT:
                # pass
                vel_x = -10
                vel_y = 0

            # Up Key
            if event.key == pygame.K_UP:
                # pass
                vel_y = - 10
                vel_x = 0

            # Down Key
            if event.key == pygame.K_DOWN:
                # pass
                vel_y = 10
                vel_x = 0


    # Snake Velocity
    snk_x = snk_x + vel_x
    snk_y = snk_y + vel_y
    



    #  Change the Background WHITE (By Default it is BLACK)
    gameWindowSize.fill(white)

    # Create a Snake with the help rect() function
    pygame.draw.rect(gameWindowSize, Red, [snk_x, snk_y, snk_len, snk_len])

    pygame.display.update()            # Display Update

    # Add fps (Frame per Second)
    clock.tick(fps)


pygame.quit()
quit()