import pygame
import time 
pygame.init()

screen = pygame.display.set_mode((600,600))

birthday = pygame.image.load("lesson 4\picture\image no.1-birthday bg.jpg")
cake = pygame.image.load("lesson 4\picture\image no.2- birthday cake.png") 
gift = pygame.image.load("lesson 4\picture\image no.3- gift.jpg")

font = pygame.font.SysFont("Times New Roman",36)

while True:
    #for event in pygame.event.get():
      #  if event.type == pygame.QUIT:
      #  pygame.quit()
    screen.fill("black")
    screen.blit(birthday,(0,0))
    text1 = font.render("happy birthday",True,"coral")
    screen.blit(text1,(200,140))
    pygame.display.update()
    time.sleep(1)
    screen.blit(cake,(100,100))
    pygame.display.update()
    time.sleep(5)
    screen.blit(gift,(0,0))
    text2 = font.render("wish you the best life",True,"coral")
    screen.blit(text2,(200,140))
    pygame.display.update()
    time.sleep(5)