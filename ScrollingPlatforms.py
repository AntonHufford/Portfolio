#a side scrolling platform game using a lot of programming concepts
#arrow keys to move, space bar to pause/unpause

import pygame
import sys
import random

pygame.init()

width = 600
height = 400
green = (139, 50, 168)
pos = pygame.math.Vector2(300, 200)
vel = pygame.math.Vector2(0, 0)
acc = pygame.math.Vector2(0, 0)
score = 0
FRICTION = -0.01

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

plat_list = [[10, 200, 60, 20],
             [150, 150, 50, 20],
             [350, 300, 150, 20],
             [500, 70, 40, 20]]

rect_list = []

player = pygame.Rect(pos.x, pos.y, 20, 20)

running = True
paused = False

for plat in plat_list:
        #pygame.draw.rect(screen, green, (plat[0], plat[1], plat[2], plat[3]))
        a = pygame.Rect(plat[0], plat[1], plat[2], plat[3])
        rect_list.append(a)
                
def get_input():
                
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_LEFT]:
        acc.x = -0.2
    if pressed[pygame.K_RIGHT]:
        acc.x = 0.2
    if pressed[pygame.K_UP]:
        acc.y = -0.2
    
def update():
        
    acc.x += vel.x * FRICTION    
    pos.x += vel.x + 0.5 * acc.x
    vel.x += acc.x
    
    acc.y += vel.y * FRICTION    
    pos.y += vel.y + 0.5 * acc.y
    vel.y += acc.y
    
    player.left = pos.x
    player.top = pos.y        
    
    for recty in rect_list:
        recty.left -= 3
        if recty.right < 0:
          rect_list.remove(recty)
          b = pygame.Rect(random.randint(width, width + 40), random.randint(50, height - 20), random.randint(40, 120), 20)
          rect_list.append(b)
          global score
          score += 10
        if recty.colliderect(player) and vel.y > 0:
            pos.y = recty.top - 19
            vel.y = 0
            
            
              
def draw():
    
    screen.fill((0, 0, 0))  
    pygame.draw.rect(screen, green, (int(pos.x), int(pos.y), 20, 20))
    pygame.display.set_caption(str(score))

    for recty in rect_list:
        pygame.draw.rect(screen, green, (recty.left, recty.top, recty.width, recty.height))
           
    pygame.display.flip()
    clock.tick(60)
    
while running:
    
    if not paused:
        acc.x = 0
        acc.y = 0.5

        get_input()
        update()
        draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x and pos.y > height - 20:
                vel.y = -15
            if event.key == pygame.K_x and vel.y == 0:
                vel.y = -15
            if event.key == pygame.K_SPACE:
                paused = not paused
                
pygame.quit()
sys.exit()  
