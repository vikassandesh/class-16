import random
import pgzrun
import time
import sys

WIDTH = 1200
HEIGHT = 600

bullets = []
ship = Actor("ship")
bug = Actor("bug")
#screen.bgcolor("black")

ship.pos = (WIDTH//2,HEIGHT//2)
enemies = []
for i in range (8):
    for k in range (4):
        enemies.append(Actor("bug"))
        enemies[-1].i = 100 + 50*i
        enemies[-1].k = 80 + 50*k

score = 0
direction = 1
ship.dead = False
ship.countdown = 90
speed = 5

def display_score():
    screen.draw.text(str(score), (50,30))
    color = "white"
    
    
def game_over():
      screen.draw.text(str("game_over"), (50,50))
      color = "white"


def on_key_down(key):
    if not ship.dead:
        if key == key.space:
            bullets.append(Actor("bullets"))
            bullets[-1].x=ship.x
            bullets[-1].y=ship.y-50
            
            
def update():
    global score, direction
    move_down = False
    
    if not ship.dead:
        if keyboard.left:
            ship.x = ship.x - speed
            if ship.x <= 0:
                ship.x = 0
            
        elif keyboard.right:
            ship.x = ship.x + speed
            if ship.x >= WIDTH:
                ship.x = WIDTH
                
    for bullet in bullets[:]:
        if bullet.y <= 0:
            bullets.remove(bullet)
        
        else:
            bullet.y = bullet.y - 10
    
    
    if len(enemies) == 0:
        game_over()
        
    if len(enemies) > 0 and (enemies[0].x < 80 or enemies[-1].x > WIDTH - 80):
        move_down = True
        direction = direction*-1
    
    for enemy in enemies:
        enemy.x += 6*direction
        if move_down == True:
            enemy.y += 1
            
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            
        for bullet in bullets:
           if enemy.colliderect(bullet):
               sounds.eep.play()
               score += 100
               bullets.remove(bullet)
               enemies.remove(enemy)
               if len(enemies) == 0: 
                   game_over()

        if enemy.colliderect(ship):
            sounds.eep.play()
            ship.dead = True
    
    if ship.dead:
        ship.countdown -=1
        
    if ship.countdown == 0:
        ship.dead = False
        ship.countdown = 90

def draw():
    screen.clear()
    screen.fill((0,0,255))
    
    for bullet in bullets:
        bullet.draw()
        
    for enemy in enemies:
        enemy.draw()
        
    if ship.dead == False:
        ship.dead()
                
    display_score()
    
    if len(enemies) == 0:
        game_over()
        
        
pgzrun.go()
        
        
        


