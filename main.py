import pygame 
from sys import exit 


# initializing pygame is absolutely necessary
pygame.init()

# creating a screen
screen = pygame.display.set_mode((800, 400))

# creating a title for window
pygame.display.set_caption("Game")

# creating a ceiling object for FPS
clock = pygame.time.Clock()

# creating a font image
test_font

# creating a surface
sky_surface = pygame.image.load('/home/saurya/code/game/graphics/Sky.png')

# creaing a ground
gorund_surface = pygame.image.load('/home/saurya/code/game/graphics/ground.png')


#makeing the loop for ever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #* placing the regular to display surface on the 
    screen.blit(sky_surface,(0,0))     #! maintain order for images
    screen.blit(gorund_surface,(0,300))

    pygame.display.update() # This updates the screen variable
    clock.tick(60)

    