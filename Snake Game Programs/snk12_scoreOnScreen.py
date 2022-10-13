# Import pygame module 
import pygame

# Import random module
import random


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
fps = 50                   # Add fps (Frame per Second)


# Snake Velocity value
vel_x = 0
vel_y = 0


# Food position 
food_x = random.randint(30, 950)        # Screen_widht value is 1000
food_y = random.randint(30, 550)       # Screen_height value is 600



#  Score Initialized
score = 0


# Set the Score on Screen
font = pygame.font.SysFont(None, 55)
def scoreOn_screen(text, color, x, y):
    scoreOn_screen = font.render(text, True, color)
    gameWindowSize.blit(scoreOn_screen, [x,y])


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
                vel_x = 5
                vel_y = 0

            #  Left Key
            if event.key == pygame.K_LEFT:
                # pass
                vel_x = -5
                vel_y = 0

            # Up Key
            if event.key == pygame.K_UP:
                # pass
                vel_y = -5
                vel_x = 0

            # Down Key
            if event.key == pygame.K_DOWN:
                # pass
                vel_y = 5
                vel_x = 0


    # Snake Velocity
    snk_x = snk_x + vel_x
    snk_y = snk_y + vel_y
    


    # snake Eat food and Score visible on console
    if abs(snk_x - food_x)<10 and abs(snk_y - food_y)<10 :
        score = score + 1
        # print("Score: ", score * 5)

        food_x = random.randint(30, 950)        # Screen_widht value is 1000
        food_y = random.randint(30, 550)       # Screen_height value is 600




    #  Change the Background WHITE (By Default it is BLACK)
    gameWindowSize.fill(white)



    # Score on Screen
    scoreOn_screen("Score: " + str(score * 5), Green, 800, 5)


    # Create a Snake with the help rect() function
    pygame.draw.rect(gameWindowSize, Red, [snk_x, snk_y, snk_len, snk_len])


    # Create a Snake food 
    pygame.draw.rect(gameWindowSize, Black, [food_x, food_y, snk_len, snk_len])


    pygame.display.update()            # Display Update

    # Add fps (Frame per Second)
    clock.tick(fps)


pygame.quit()
quit()