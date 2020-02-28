import pygame 
pygame.init()

windows = pygame.display.set_mode((800,600))
pygame.display.set_caption("My Game")

icon = pygame.image.load("C:\\Users\\Benjamin\\Desktop\\Neuer Ordner\\super-mario.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("C:\\Users\\Benjamin\\Desktop\\player.png")
playerx = 300
playery = 300

def player(x,y):
    windows.blit(playerImg,(playerx, playery))

isJump = False
jumpCount = 11

vel = 20

run = True
while run:
    pygame.time.delay(30) 
    windows.fill((45, 79, 194))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False    

    direction = pygame.key.get_pressed()
    if direction[pygame.K_LEFT]:
        playerx -= vel
    if direction[pygame.K_RIGHT]: 
        playerx += vel

    
    if direction[pygame.K_SPACE]:
        isJump = True
    


    if playerx <= 0:
        playerx = 0
    if playerx >= 736:
        playerx = 736
    if playery <= 0:
        playery = 0
    if playery >= 536:
        playery = 536
    
    if not(isJump):
        if direction[pygame.K_UP] and playery > vel:
            playery -= vel
        
        if direction[pygame.K_DOWN] and playery < 600 - vel:
            playery += vel
        
        if direction[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -11:
            playery -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1 
        else:
            jumpCount = 11
            isJump = False
    player(playerx,playery)
    pygame.display.update()
pygame.quit()
