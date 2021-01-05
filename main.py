import pygame

#Initialize pygame to get all the methods
pygame.init()

#This creates the screen
screen = pygame.display.set_mode((800, 600))

'''
This will let the window open but there is nothing so it froze 
while True:
    pass
'''

# Game loop to make sure game is running always
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False