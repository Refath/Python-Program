import pygame
import time

pygame.init()
white = (34,34,34)
black=(0,0,0)
red=(255,0,0)
led=45
pik=105
silver=(110,108,108)
yellow=(193,206,104)
yellow2=(213,230,100)
display_height=600
display_width=800
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Find the SLENDERMAN')

gameExit=False


lead_x = 300
lead_y = 300
lead_z=1
ps=-43+300
background_color=black
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
                print("LEFT")
                lead_z -=10
            if event.key == pygame.K_RIGHT:
                lead_x +=10
                print("RIGHT")
                lead_z +=10
            if event.key == pygame.K_UP:
                 lead_y -=10
                 print("UP")
                 lead_z -=10
            if event.key == pygame.K_DOWN:
                 lead_y +=10
                 print("DOWN")
                 lead_z +10
            if event.key == pygame.K_a:
                gameDisplay.fill(red)
                led +=10
                ps -=5
            if led == 95:
                background_color=red
                print("YOU FOUND M E !")
             
                
    gameDisplay.fill(background_color)
    pygame.draw.ellipse(gameDisplay, black,[-295+300-lead_z,-54+300,75,100])
    pygame.draw.ellipse(gameDisplay, red,[-285+300-lead_z,-35+300,20,34])
    pygame.draw.ellipse(gameDisplay, red,[-255+300-lead_z,-35+300,20,34])
    pygame.draw.rect(gameDisplay, silver,[300+lead_x,-35+lead_y,75,30])
    pygame.draw.ellipse(gameDisplay, yellow,[505+lead_z,ps,105,led])

    pygame.draw.circle(gameDisplay, yellow, (750+lead_z, 200), 75, 0)
    pygame.draw.ellipse(gameDisplay, white,[680+lead_z,ps-80,50,led])
    pygame.draw.line(gameDisplay, white, [730+lead_z, 450], [730+lead_z,273], 10)
    

    pygame.display.update()

pygame.quit()
quit()
