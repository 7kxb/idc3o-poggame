import pygame
import os
import sys
sys.path.insert(0,os.path.join('3 - pong','logic'))
from define import *

WIDTH,HEIGHT,WIN,WHITE,BLACK,YELLOW,RED,BORDER,HEALTH_FONT,POWER_FONT,WINNER_FONT,BULLET_HIT_SOUND,BULLET_FIRE_SOUND,BOUNCE_SOUND,ROUND_SOUND,SAGE_WALL,MUSIC,FPS,VEL,BULLET_VEL,MAX_BULLETS,YELLOW_HIT,RED_HIT,YELLOW_POINT,RED_POINT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT,YELLOW_SPACESHIP_IMAGE,YELLOW_SPACESHIP,RED_SPACESHIP_IMAGE,RED_SPACESHIP,SPACE,RED_ROCKET_IMAGE,RED_ROCKET,YELLOW_ROCKET_IMAGE,YELLOW_ROCKET,EXPLOSION_IMAGE,EXPLOSION = define()

def red_handle_movement(keys_pressed,red,pygame):
    if keys_pressed[pygame.K_i] and red.y - VEL > HEIGHT//6:
        red.y -= VEL
    if keys_pressed[pygame.K_j] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -= VEL
    if keys_pressed[pygame.K_k] and red.y + VEL + red.height < HEIGHT+SPACESHIP_HEIGHT//20:
        red.y += VEL
    if keys_pressed[pygame.K_l] and red.x + VEL + red.width < WIDTH+SPACESHIP_WIDTH//20:
        red.x += VEL