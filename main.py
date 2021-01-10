''' Jennifer Villalba
01/09/2020
Pygame Tutorial for Beginners - Python Game Development Course
by: freeCodeCamp.org '''
import math
import random
import pygame

# Initialize pygame to get all the methods
pygame.init()  # always here

# This creates the screen
# w -> 800 H -> 600 middle is 300
screen = pygame.display.set_mode((800, 600))

# Add the ship
shipPlayer = pygame.image.load('flying-rocket.png')
# Coordinates where we want the ship to appear
shipX = 300
shipY = 500
shipX_change = 0

# Add the enemy
# add more than one cherry/enemy
cherry = []
cherryX = []
cherryY = []
cherryX_change = []
cherryY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    cherry.append(pygame.image.load('happyCherry.png'))
    # Coordinates where we want the ship to appear
    cherryX.append(random.randint(0, 800))
    cherryY.append(random.randint(50, 150))
    cherryX_change.append(0.45)
    cherryY_change.append(40)

# Add the fire
# Ready - you cannot see the "bullet" on screen
fire = pygame.image.load('fire-flame-.png')
# Coordinates where we want the ship to appear
fireX = 0
fireY = 480
fireX_change = 0
fireY_change = 0.32
fire_state = 'ready'


score = 0
# to add more fonts we will have to go to a website and extract ttf file
font = pygame.font.Font('freesansbold.ttf', 32)

testX = 10
testY = 10


def show_score(x, y):
    scoreVal = font.render("Score :" + str(score), True, (255, 255, 255))
    screen.blit(scoreVal, (x, y))


# Title for the window
pygame.display.set_caption("Jennifer Cherry Space")
# Icon from 'flaticon.com'
icon = pygame.image.load('cherrry.png')
pygame.display.set_icon(icon)


def ship(x, y):
    # image and X,Y coordinates
    screen.blit(shipPlayer, (shipX, shipY))  # blit = to draw


def cherry_enemy(x, y, i):
    # image and X,Y coordinates
    screen.blit(cherry[i], (x, y))  # blit = to draw


def fire_fire(x, y):
    global fire_state
    fire_state = "fire"
    screen.blit(fire, (x + 16, y + 10))


def isCollision(cherryX, cherryY, fireX, fireY):
    distance = math.sqrt((math.pow(cherryX - fireX, 2)) + (math.pow(cherryY - fireY, 2)))
    if distance < 27:
        return True
    return False


# Game loop to make sure game is running always
running = True

while running:
    # Change Background Color window
    screen.fill((100, 0, 40))  # RGB = (red, green, blue) 0-256

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check if keystroke is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                shipX_change = -0.3
            if event.key == pygame.K_RIGHT:
                shipX_change = 0.3
            if event.key == pygame.K_SPACE:
                if fire_state == "ready":
                    fireX = shipX
                    fire_fire(fireX, fireY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                shipX_change = 0  # stop the ship from moving

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 - 5 + 0.1

    shipX += shipX_change
    # add boundaries to the ship to now go outside the window
    if shipX <= 0:
        shipX = 0
    elif shipX >= 736:
        shipX = 736

    for i in range(num_of_enemies):
        cherryX[i] += cherryX_change[i]
        # add boundaries to the cherry to now go outside the window
        if cherryX[i] <= 0:
            cherryX_change[i] = 0.25
            cherryY[i] += cherryY_change[i]
        elif cherryX[i] >= 736:
            cherryX_change[i] = -0.25
            cherryY[i] += cherryY_change[i]

        # collision
        collision = isCollision(cherryX[i], cherryY[i], fireX, fireY)
        if collision:  # what to do if cherry gets hit
            fireY = 480
            fire_state = "ready"
            score += 1
            cherryX[i] = random.randint(0, 800)
            cherryY[i] = random.randint(50, 150)

        cherry_enemy(cherryX[i], cherryY[i], i)

    # Fire movement
    if fireY <= 0:  # Take bullet/fire back to ship to be able to shoot again
        fireY = 480
        fire_state = 'ready'

    if fire_state == "fire":
        fire_fire(fireX, fireY)
        fireY -= fireY_change

    ship(shipX, shipY)
    show_score(testX, testY)
    # need to updated
    pygame.display.update()  # need to updated always
