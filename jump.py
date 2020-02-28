import pygame 
pygame.init()

windows = pygame.display.set_mode((800,600))
pygame.display.set_caption("My Game")
icon = pygame.image.load("super-mario.png")
pygame.display.set_icon(icon)

x = 50 
y = 50 
width = 40
height = 60
speed = 5

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    

pygame.quit()
