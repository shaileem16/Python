import pygame
import time
import random
pygame.init()
start_time = time.time()
x=0
y=0
flag = 2
car_width = 94
lane_width = 900/3
enemy_y = -100
player_y = 400
screen_width=900
screen_height=600
enemies = [ ]
player_h=200
#background_img = pygame.image.load('road.png')
screen = pygame.display.set_mode((screen_width,screen_height))
background_img = pygame.image.load('road.png')
player_img = pygame.image.load('game_sprite.png')
enemy_img = pygame.image.load('enemy.png')
def move_background(road_x,road_y,screen_height,screen,road_img):
    rel_y=road_y%screen_height
    #print("rel_y {}".format(rel_y))
    screen.blit(road_img,(road_x,rel_y-screen_height))  
    #print("rel_y-height {}".format(rel_y-screen_height))
    if rel_y<screen_height:
        screen.blit(road_img,(x,rel_y))
    road_y+=10
    return road_y

def generate_enemies(enemy_y,lane_width,enemies,car_width):
    flag = random.randrange(1,4,1)
    enemies.append([int(flag * lane_width - (lane_width + car_width)/2),enemy_y,flag])

def enemy_moment(enemies,game_screen,sprite_img):
    if len(enemies)<=0 : return
    for enemy in enemies:
        game_screen.blit(sprite_img,(enemy[0],enemy[1]))
        enemy[1]+=10
def splice_enemies(enemies):
    for enemy in enemies:
        if enemy[1]>=600:
            index_enemy=enemies.index(enemy)
            enemies.pop(index_enemy)
    return enemies
def car_collision(enemies,player_y,player_h,flag):
    for enemy in enemies:
        if enemy[2]==flag and enemy[1]+player_h>=player_y:
            print("collision")

running = True
while running:
    car_collision(enemies,player_y,player_h,flag) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                if flag <= 1:
                    continue
                flag-=1
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                if flag >= 3:
                    continue
                flag+=1 
        if event.type == pygame.KEYUP:
            pass
        player_x =int( flag * lane_width - (lane_width + car_width)/2)
    if time.time()-start_time>3:
        start_time = time.time()
        generate_enemies(enemy_y,lane_width,enemies,car_width)
    y=move_background(x,y,screen_height,screen,background_img)
    screen.blit(player_img,(player_x,player_y)) 
    enemy_moment(enemies,screen,enemy_img)

    pygame.display.update()
    enemies=splice_enemies(enemies)
    