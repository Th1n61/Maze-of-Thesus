import pygame
from pygame.locals import *

pygame.init()
width=460
height=300
screen = pygame.display.set_mode((width, height))
background = (255,255,255)
screen.fill(background)
caption = 'Maze of Thesus'
pygame.display.set_caption(caption)
pygame.display.update()
#pygame.mixer.Sound()
x = -5404
y = -4763
middlex=int(width/2)
middley=int(height/2)
x_old=0
y_old = 0
x_change=0
y_change=0
speed = 0.2
zoom = 50
zoomchange=0
eg=False
offSet=6.5
maze = pygame.image.load("r.gif")
maze = pygame.transform.scale(maze, (228*zoom, 180*zoom))
maze.convert()
answer = pygame.image.load("rb.gif")
answer = pygame.transform.scale(answer, (228*zoom,180*zoom))#1017x761/4.4605263x((2.21/2)*zoom), ((2.536666/2)*zoom))
answer.convert()
player = pygame.image.load("player1.jpg")
player = pygame.transform.scale(player, (20,20))
player.convert()
rect = player.get_rect()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
  
      
    elif event.type == KEYDOWN:
      if event.key == K_UP:
        y_change = speed
        
      elif event.key == K_DOWN:
        y_change = -speed
        
      elif event.key == K_RIGHT:
        x_change = -speed

      elif event.key == K_LEFT:
        x_change = speed

      elif event.key == K_a:
        eg=True
        
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        x_change = 0
      elif event.key == K_UP or event.key == K_DOWN:
        y_change = 0
      elif event.key == K_a:
        eg=False
        
  screen.fill((255,255,255))
  x_old = x
  y_old = y
  x += x_change
  y += y_change

  if eg:
    screen.blit(answer,(x+offSet,y+offSet))
  screen.blit(maze,(x,y))
  if screen.get_at((middlex, middley))[:3]==(0,0,0) or screen.get_at(((middlex+20), middley))[:3]==(0,0,0) or screen.get_at((middlex, (middley+20)))[:3]==(0,0,0) or screen.get_at(((middlex+20), (middley+20)))[:3]==(0,0,0):
    x=x_old
    y=y_old
    screen.fill((255,255,255))
    if eg:
      screen.blit(answer,(x+offSet,y+offSet))
    screen.blit(maze,(x,y))
  screen.blit(player,(width/2,height/2))
  pygame.display.update()
