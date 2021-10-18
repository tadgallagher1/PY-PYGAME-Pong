
# Import the pygame library and initialise the game engine
import pygame
from paddle import Paddle
pygame.init()

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Open a new window
size = (700, 500)
screen  = pygame.display.set_mode(size)
pygame.display.set_caption("My Pong Game!")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

"""
1) Capturing Events: Used to constantly “listen” to user inputs and react to these. 
It could be when the user use the keyboard or the mouse.
2) Implementing the Game Logic. What happens when the game is running? Are cars moving forward, 
aliens falling from the sky, ghosts chasing you, etc.
3) Refreshing the screen by redrawing the stage and the sprites.

"""

#--------------------Main Loop--------------------------------
while carryOn: 
    # Main event loop 
    for event in pygame.event.get():  # The user did something
        if event.type == pygame.QUIT:  # If the user clicked close (upper corner) 
            carryOn = false  # Exit loop
            
    # --- Game logic should go here
    
    
    
    # --- Drawing code should go here
    # Clear/Fill the screen with black
    screen.fill(BLACK)
    # Draw the net / lines
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)
    
    # Draw the screen
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(60) 
    
pygame.quit()            