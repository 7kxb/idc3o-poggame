import pygame
import os
import json
#import random
#from pygame.locals import *

with open(os.path.join('3 - pong','logic','res.json'),"r") as openfile:
        res_json_file = json.load(openfile)
        WIDTH = res_json_file["width"]
        HEIGHT = res_json_file["height"]

def define():
    #temp = random.randint(1,15)
    pygame.font.init()
    pygame.mixer.init()
    #flags = FULLSCREEN | DOUBLEBUF
    global WIDTH,HEIGHT
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    #WIN = pygame.display.set_mode((WIDTH,HEIGHT),flags,16)
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    YELLOW = (255,255,0)
    RED = (255,40,40)
    BORDER = pygame.Rect(WIDTH//2-WIDTH//100,0,WIDTH//50,HEIGHT)
    STAT_FONT = pygame.font.SysFont('comicsans',WIDTH//16)
    FPS_FONT = pygame.font.SysFont('comicsans',WIDTH//32)
    WINNER_FONT = pygame.font.SysFont('comicsans',WIDTH//8)
    BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('3 - pong','assets','hit.mp3'))
    BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('3 - pong','assets','fire.mp3'))
    BOUNCE_SOUND = pygame.mixer.Sound(os.path.join('3 - pong','assets','bounce.mp3'))
    ROUND_SOUND = pygame.mixer.Sound(os.path.join('3 - pong','assets','round.mp3'))
    SAGE_WALL = pygame.mixer.Sound(os.path.join('3 - pong','assets','sage_wall.mp3'))
    #MUSIC = pygame.mixer.Sound(os.path.join('3 - pong','assets','mus_'+str(temp)+'.mp3'))
    FPS = 120
    file1 = open(os.path.join('3 - pong','logic','vel.txt'),"r")
    SPEED = int(file1.read())
    file1.close()
    VEL = (WIDTH*HEIGHT)//(SPEED*2)
    if SPEED == 48000:
        MUSIC = pygame.mixer.Sound(os.path.join('3 - pong','assets','turtle.mp3'))
    if SPEED == 42000:
        MUSIC = pygame.mixer.Sound(os.path.join('3 - pong','assets','pacificrim.mp3'))
    if SPEED == 36000:
        MUSIC = pygame.mixer.Sound(os.path.join('3 - pong','assets','lastingpromise.mp3'))
    BULLET_VEL = (WIDTH*HEIGHT)//(288000/4)
    MAX_BULLETS = 0
    YELLOW_HIT = pygame.USEREVENT + 1
    RED_HIT = pygame.USEREVENT + 2
    YELLOW_POINT = pygame.USEREVENT + 3
    RED_POINT = pygame.USEREVENT + 4
    SPACESHIP_WIDTH,SPACESHIP_HEIGHT = WIDTH//10,HEIGHT//10
    YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('3 - pong','assets','spaceship_yellow.png')).convert_alpha()
    YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
    RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('3 - pong','assets','spaceship_red.png')).convert_alpha()
    RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),180)
    SPACE = pygame.transform.scale(pygame.image.load(os.path.join('3 - pong','assets','space.png')).convert(),(WIDTH,HEIGHT-HEIGHT//6))
    RED_ROCKET_IMAGE = pygame.image.load(os.path.join('3 - pong','assets','RED_ROCKET.png')).convert_alpha()
    RED_ROCKET = pygame.transform.scale(RED_ROCKET_IMAGE,(SPACESHIP_WIDTH//2,SPACESHIP_HEIGHT//4))
    YELLOW_ROCKET_IMAGE = pygame.image.load(os.path.join('3 - pong','assets','YELLOW_ROCKET.png')).convert_alpha()
    YELLOW_ROCKET = pygame.transform.scale(YELLOW_ROCKET_IMAGE,(SPACESHIP_WIDTH//2,SPACESHIP_HEIGHT//4))
    EXPLOSION_IMAGE = pygame.image.load(os.path.join('3 - pong','assets','explosion.png')).convert_alpha()
    EXPLOSION = pygame.transform.scale(EXPLOSION_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))

    return WIDTH,HEIGHT,WIN,WHITE,BLACK,YELLOW,RED,BORDER,STAT_FONT,FPS_FONT,WINNER_FONT,BULLET_HIT_SOUND,BULLET_FIRE_SOUND,BOUNCE_SOUND,ROUND_SOUND,SAGE_WALL,MUSIC,FPS,VEL,BULLET_VEL,MAX_BULLETS,YELLOW_HIT,RED_HIT,YELLOW_POINT,RED_POINT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT,YELLOW_SPACESHIP_IMAGE,YELLOW_SPACESHIP,RED_SPACESHIP_IMAGE,RED_SPACESHIP,SPACE,RED_ROCKET_IMAGE,RED_ROCKET,YELLOW_ROCKET_IMAGE,YELLOW_ROCKET,EXPLOSION_IMAGE,EXPLOSION