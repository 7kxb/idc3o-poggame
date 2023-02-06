################
# File Name: main_menu.py
# Description: Top Layer
# Authors: Kevin X. Chongyang W. Steven M.
# Date: 2022 - 09 - 17
################
def re():
# putting the entire main code in a function to be called if resolution is pressed
    import pygame
    # imports pygame
    import os
    # imports os
    import sys
    # imports sys
    import json
    # imports json
    sys.path.insert(0,os.path.join('3 - pong','logic'))
    # inserts logic folder into sys path
    from check import hi,close,select
    # imports 3 functions from a file
    sys.path.insert(0,os.path.join('3 - pong','index'))
    # inserts index folder into sys path
    import pongame1
    # imports singleplayer pongame
    import pongame2
    # imports multiplayer pongame
    pygame.font.init()
    # initializes the font into pygame
    pygame.mixer.init()
    # initializes the mixer into pygame
    with open(os.path.join('3 - pong','logic','res.json'),"r") as openfile:
    # opens res.json as read only
        res_json_file = json.load(openfile)
        # puts load into variable
        WIDTH = res_json_file["width"]
        # assigns width from res.json into variable width
        HEIGHT = res_json_file["height"]
        # assigns height from res.json into variable height
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    # initializes the window as variable WIN
    pygame.display.set_caption('pongame')
    # assigns caption 'pongame' to the window
    WHITE = (255,255,255)
    # assigns hex code #FFFFFF to variable WHITE
    BLACK = (0,0,0)
    # assigns hex code #000000 to variable BLACK
    YELLOW = (255,255,0)
    # assigns hex code #FFFF00 to variable YELLOW
    BLUE = (0,0,255)
    # assigns hex code #0000FF to variable BLUE
    RED = (255,0,0)
    # assigns hex code #FF0000 to variable RED
    GREEN = (0,255,0)
    # assigns hex code #00FF00 to variable GREEN
    FONT_0 = pygame.font.SysFont('comicsans',WIDTH//4)
    # creates a new font using 'comicsans' with size WIDTH//4
    FONT_1 = pygame.font.SysFont('comicsans',WIDTH//19)
    # creates a new font using 'comicsans' with size WIDTH//19
    MUSIC = pygame.mixer.Sound(os.path.join('3 - pong','assets','happy.mp3'))
    # creates a new sound using happy.mp3
    FPS = 60
    # sets fps cap to 60
    VEL = (WIDTH*HEIGHT)//(288000/2)
    # sets velocity to (WIDTH*HEIGHT)//(288000/2)
    BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('3 - pong','assets','background.jpg')),(WIDTH,HEIGHT))
    # creates the background using background.jpg
    PLAY_BUTTON_0 = pygame.Rect(WIDTH//2-WIDTH//6,HEIGHT//2+HEIGHT//8-HEIGHT//8,WIDTH//3,HEIGHT//6)
    # creates a rectangle for a button
    CONFIG_BUTTON_0 = pygame.Rect(WIDTH//2-WIDTH//6,HEIGHT//2+HEIGHT//8+HEIGHT//8,WIDTH//3,HEIGHT//6)
    # creates a rectangle for a button
    PLAY_BUTTON_0h = pygame.Rect(WIDTH//2-WIDTH//5.6,HEIGHT//2+HEIGHT//8-HEIGHT//8,WIDTH//2.8,HEIGHT//6)
    # creates a rectangle for a button
    CONFIG_BUTTON_0h = pygame.Rect(WIDTH//2-WIDTH//5.6,HEIGHT//2+HEIGHT//8+HEIGHT//8,WIDTH//2.8,HEIGHT//6)
    # creates a rectangle for a button
    RES_A_3 = pygame.Rect(WIDTH//2-WIDTH//6,HEIGHT//2+HEIGHT//8-HEIGHT//8,WIDTH//3,HEIGHT//6)
    # unused, i forgot what this does
    RES_B_3 = pygame.Rect(WIDTH//2-WIDTH//6,HEIGHT//2+HEIGHT//8-HEIGHT//8,WIDTH//3,HEIGHT//6)
    # unused too, i forgot what this does too
    BACK_BUTTON_3 = pygame.Rect(WIDTH//2-WIDTH//6,HEIGHT//2+HEIGHT//8+HEIGHT//8,WIDTH//3,HEIGHT//6)
    # creates a rectangle for a button
    def draw_window(menu,highlight):
        # main draw window loop function
        WIN.fill(BLACK)
        # fill the window with black
        WIN.blit(BACKGROUND,(0,0))
        # blit the background layered on top of the black
        if menu == 1:
        # if menu is the first one, run the indented code
            if highlight % 2 == 0:
            # if the first button is highlighted, run the indented code
                pygame.draw.rect(WIN,GREEN,PLAY_BUTTON_0h)
                # highlights the first button visually/graphically
            if highlight % 2 == 1:
            # if the second button is highlighted, run the indented code
                pygame.draw.rect(WIN,GREEN,CONFIG_BUTTON_0h)
                # highlights the seconds button visually/graphically
            title = FONT_0.render('POGAME',1,WHITE)
            # creates text 'POGAME'
            WIN.blit(title,(WIDTH//2-title.get_width()//2,HEIGHT//4-HEIGHT//8))
            # blits the title text
            pygame.draw.rect(WIN,WHITE,PLAY_BUTTON_0)
            # draws the play button
            pygame.draw.rect(WIN,WHITE,CONFIG_BUTTON_0)
            # draws the config button
            play = FONT_1.render('PLAY',1,BLACK)
            # creates text 'PLAY'
            WIN.blit(play,(WIDTH//2-play.get_width()//2,HEIGHT//2+HEIGHT//6-HEIGHT//8))
            # blits the play text ontop of the button
            config = FONT_1.render('CONFIG',1,BLACK)
            # creates text 'CONFIG'
            WIN.blit(config,(WIDTH//2-config.get_width()//2,HEIGHT//2+HEIGHT//6+HEIGHT//8))
            # blits the config text ontop of the button
        if menu == 2:
            if highlight % 3 == 0:
                pygame.draw.rect(WIN,GREEN,pygame.Rect(WIDTH//2-WIDTH//5.6,HEIGHT//2+HEIGHT//8-HEIGHT//3,WIDTH//2.8,HEIGHT//6))
            if highlight % 3 == 1:
                pygame.draw.rect(WIN,GREEN,PLAY_BUTTON_0h)
            if highlight % 3 == 2:
                pygame.draw.rect(WIN,GREEN,CONFIG_BUTTON_0h)
            pygame.draw.rect(WIN,WHITE,pygame.Rect(WIDTH//2-WIDTH//6,HEIGHT//2+HEIGHT//8-HEIGHT//3,WIDTH//3,HEIGHT//6))
            play = FONT_1.render('SINGLEPLAYER',1,BLACK)
            WIN.blit(play,(WIDTH//2-play.get_width()//2,HEIGHT//2+HEIGHT//6-HEIGHT//3))
            pygame.draw.rect(WIN,WHITE,PLAY_BUTTON_0)
            play = FONT_1.render('MULTIPLAYER',1,BLACK)
            WIN.blit(play,(WIDTH//2-play.get_width()//2,HEIGHT//2+HEIGHT//6-HEIGHT//8))
            pygame.draw.rect(WIN,WHITE,BACK_BUTTON_3)
            back = FONT_1.render('BACK TO MENU',1,BLACK)
            WIN.blit(back,(WIDTH//2-back.get_width()//2,HEIGHT//2+HEIGHT//6+HEIGHT//8))
        if menu == 3:
            if highlight % 3 == 0:
                pygame.draw.rect(WIN,GREEN,pygame.Rect(WIDTH//2-WIDTH//5.6,HEIGHT//2+HEIGHT//8-HEIGHT//3,WIDTH//2.8,HEIGHT//6))
            if highlight % 3 == 1:
                pygame.draw.rect(WIN,GREEN,PLAY_BUTTON_0h)
            if highlight % 3 == 2:
                pygame.draw.rect(WIN,GREEN,CONFIG_BUTTON_0h)
            pygame.draw.rect(WIN,WHITE,pygame.Rect(WIDTH//2-WIDTH//6,HEIGHT//2+HEIGHT//8-HEIGHT//3,WIDTH//3,HEIGHT//6))
            gfx = FONT_1.render('VISUAL GRAPHIC',1,BLACK)
            WIN.blit(gfx,(WIDTH//2-gfx.get_width()//2,HEIGHT//2+HEIGHT//6-HEIGHT//3))
            pygame.draw.rect(WIN,WHITE,PLAY_BUTTON_0)
            play = FONT_1.render('CREDITS',1,BLACK)
            WIN.blit(play,(WIDTH//2-play.get_width()//2,HEIGHT//2+HEIGHT//6-HEIGHT//8))
            pygame.draw.rect(WIN,WHITE,BACK_BUTTON_3)
            back = FONT_1.render('BACK TO MENU',1,BLACK)
            WIN.blit(back,(WIDTH//2-back.get_width()//2,HEIGHT//2+HEIGHT//6+HEIGHT//8))
        if menu == 4:
            pygame.draw.rect(WIN,WHITE,BACK_BUTTON_3)
            wait = FONT_1.render('LOADING...',1,BLACK)
            WIN.blit(wait,(WIDTH//2-wait.get_width()//2,HEIGHT//2+HEIGHT//6+HEIGHT//8))
        if menu == 5:
            text1 = FONT_1.render('Code: Kevin X',1,WHITE)
            text2 = FONT_1.render('Design: Chongyang W, Steven M',1,WHITE)
            if highlight % 1 == 0:
                pygame.draw.rect(WIN,GREEN,CONFIG_BUTTON_0h)
            WIN.blit(text1,(WIDTH//2-text1.get_width()//2,HEIGHT//4-HEIGHT//8))
            WIN.blit(text2,(WIDTH//2-text2.get_width()//2,HEIGHT//4))
            pygame.draw.rect(WIN,WHITE,BACK_BUTTON_3)
            back = FONT_1.render('BACK',1,BLACK)
            WIN.blit(back,(WIDTH//2-back.get_width()//2,HEIGHT//2+HEIGHT//6+HEIGHT//8))
        if menu == 6:
            if highlight % 3 == 0:
                pygame.draw.rect(WIN,GREEN,pygame.Rect(WIDTH//2-WIDTH//5.6,HEIGHT//2+HEIGHT//8-HEIGHT//3,WIDTH//2.8,HEIGHT//6))
            if highlight % 3 == 1:
                pygame.draw.rect(WIN,GREEN,PLAY_BUTTON_0h)
            if highlight % 3 == 2:
                pygame.draw.rect(WIN,GREEN,CONFIG_BUTTON_0h)
            pygame.draw.rect(WIN,WHITE,pygame.Rect(WIDTH//2-WIDTH//6,HEIGHT//2+HEIGHT//8-HEIGHT//3,WIDTH//3,HEIGHT//6))
            eye = FONT_1.render('EYE CANDY',1,BLACK)
            WIN.blit(eye,(WIDTH//2-eye.get_width()//2,HEIGHT//2+HEIGHT//6-HEIGHT//3))
            pygame.draw.rect(WIN,WHITE,PLAY_BUTTON_0)
            res = FONT_1.render('RESOLUTION',1,BLACK)
            WIN.blit(res,(WIDTH//2-res.get_width()//2,HEIGHT//2+HEIGHT//6-HEIGHT//8))
            pygame.draw.rect(WIN,WHITE,BACK_BUTTON_3)
            back = FONT_1.render('BACK TO MENU',1,BLACK)
            WIN.blit(back,(WIDTH//2-back.get_width()//2,HEIGHT//2+HEIGHT//6+HEIGHT//8))
        if menu == 7:
            if highlight % 3 == 0:
                pygame.draw.rect(WIN,GREEN,pygame.Rect(WIDTH//2-WIDTH//5.6,HEIGHT//2+HEIGHT//8-HEIGHT//3,WIDTH//2.8,HEIGHT//6))
            if highlight % 3 == 1:
                pygame.draw.rect(WIN,GREEN,PLAY_BUTTON_0h)
            if highlight % 3 == 2:
                pygame.draw.rect(WIN,GREEN,CONFIG_BUTTON_0h)
            pygame.draw.rect(WIN,WHITE,pygame.Rect(WIDTH//2-WIDTH//6,HEIGHT//2+HEIGHT//8-HEIGHT//3,WIDTH//3,HEIGHT//6))
            eye = FONT_1.render('CLUELESS',1,BLACK)
            WIN.blit(eye,(WIDTH//2-eye.get_width()//2,HEIGHT//2+HEIGHT//6-HEIGHT//3))
            pygame.draw.rect(WIN,WHITE,PLAY_BUTTON_0)
            res = FONT_1.render('REALIZATION',1,BLACK)
            WIN.blit(res,(WIDTH//2-res.get_width()//2,HEIGHT//2+HEIGHT//6-HEIGHT//8))
            pygame.draw.rect(WIN,WHITE,BACK_BUTTON_3)
            back = FONT_1.render('AWARE',1,BLACK)
            WIN.blit(back,(WIDTH//2-back.get_width()//2,HEIGHT//2+HEIGHT//6+HEIGHT//8))
        pygame.display.update()
        # updates the pygame display window
    def main2():
    # main loop function
        clock = pygame.time.Clock()
        # clock
        run = True
        # run is always true unless user wants to quit
        menu = 1
        # set back to first menu
        highlight = 0
        # set back to first button to be highlighted
        frame_tick = 0
        # creates timed event
        while run:
        # while the program is running
            clock.tick(FPS)
            # refresh every frame
            if frame_tick <= 90:
            # before the 91st frame
                frame_tick += 1
                # add 1 to the count
                CLUELESS_IMAGE = pygame.image.load(os.path.join('3 - pong','assets','clueless.png')).convert_alpha()
                # load the image
                CLUELESS = pygame.transform.rotate(pygame.transform.scale(CLUELESS_IMAGE,(WIDTH//4,HEIGHT//4)),frame_tick*4)
                # configure the image
                WIN.blit(CLUELESS,(0,0))
                # blit the image
                pygame.display.update()
                # update the pygame display window
            if frame_tick == 90:
                MUSIC.play(-1)
                # if the frame_tick is equal to 90, start playing the music, loop after it finishes
            if frame_tick > 90:
            # after the intro logo, run the rest of the main menu loop
                for event in pygame.event.get():
                # handles events
                    if event.type == pygame.QUIT:
                    # if close button is pressed, close the game
                        run = close(pygame)
                        # this just quits
                    if event.type == pygame.KEYDOWN:
                    # if a key is pressed down
                        highlight += select(event,pygame)
                        if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                            if menu == 1:
                                if highlight % 2 == 0:
                                    menu = 0
                                    draw_window(menu,highlight)
                                    pygame.time.delay(100)
                                    menu = 7
                                if highlight % 2 == 1:
                                    menu = 0
                                    draw_window(menu,highlight)
                                    pygame.time.delay(100)
                                    menu = 3
                            elif menu == 2:
                                if highlight % 3 == 0:
                                    MUSIC.stop()
                                    menu = 4
                                    draw_window(menu,highlight)
                                    pongame1.main()
                                if highlight % 3 == 1:
                                    MUSIC.stop()
                                    menu = 4
                                    draw_window(menu,highlight)
                                    pongame2.main()
                                if highlight % 3 == 2:
                                    menu = 0
                                    draw_window(menu,highlight)
                                    pygame.time.delay(100)
                                    menu = 1
                            elif menu == 3:
                                if highlight % 3 == 0:
                                    menu = 0
                                    draw_window(menu,highlight)
                                    pygame.time.delay(100)
                                    menu = 6
                                if highlight % 3 == 1:
                                    menu = 0
                                    draw_window(menu,highlight)
                                    pygame.time.delay(100)
                                    menu = 5
                                if highlight % 3 == 2:
                                    menu = 0
                                    draw_window(menu,highlight)
                                    pygame.time.delay(100)
                                    menu = 1
                            elif menu == 5:
                                if highlight % 1 == 0:
                                    menu = 0
                                    draw_window(menu,highlight)
                                    pygame.time.delay(100)
                                    menu = 3
                            elif menu == 6:
                                if highlight % 3 == 0:
                                    file1 = open(os.path.join('3 - pong','logic','eye.txt'),"r")
                                    toggle = int(file1.read())
                                    file1.close()
                                    if toggle == 0:
                                        file1 = open(os.path.join('3 - pong','logic','eye.txt'),"w")
                                        file1.write('1')
                                        file1.close()
                                        print('toggle changed from 0 to 1')
                                    if toggle == 1:
                                        file1 = open(os.path.join('3 - pong','logic','eye.txt'),"w")
                                        file1.write('0')
                                        file1.close()
                                        print('toggle changed from 1 to 0')
                                if highlight % 3 == 1:
                                    if WIDTH == 800:
                                        resolution = {"width": 960,"height": 720}
                                        json_object = json.dumps(resolution, indent=4)
                                        with open(os.path.join('3 - pong','logic','res.json'),"w") as outfile:
                                            outfile.write(json_object)
                                    if WIDTH == 960:
                                        resolution = {"width": 800,"height": 600}
                                        json_object = json.dumps(resolution, indent=4)
                                        with open(os.path.join('3 - pong','logic','res.json'),"w") as outfile:
                                            outfile.write(json_object)
                                    MUSIC.stop()
                                    re()
                                if highlight % 3 == 2:
                                    menu = 0
                                    draw_window(menu,highlight)
                                    pygame.time.delay(100)
                                    menu = 3
                            elif menu == 7:
                                if highlight % 3 == 0:
                                    menu = 0
                                    draw_window(menu,highlight)
                                    file1 = open(os.path.join('3 - pong','logic','vel.txt'),"w")
                                    file1.write('48000')
                                    file1.close()
                                    pygame.time.delay(100)
                                    menu = 2
                                if highlight % 3 == 1:
                                    menu = 0
                                    draw_window(menu,highlight)
                                    file1 = open(os.path.join('3 - pong','logic','vel.txt'),"w")
                                    file1.write('42000')
                                    file1.close()
                                    pygame.time.delay(100)
                                    menu = 2
                                if highlight % 3 == 2:
                                    menu = 0
                                    draw_window(menu,highlight)
                                    file1 = open(os.path.join('3 - pong','logic','vel.txt'),"w")
                                    file1.write('36000')
                                    file1.close()
                                    pygame.time.delay(100)
                                    menu = 2
                        elif event.key == pygame.K_ESCAPE:
                            menu = 0
                            draw_window(menu,highlight)
                            pygame.time.delay(100)
                            menu = 1
                draw_window(menu,highlight)
    if __name__ == "__main__":
        main2()
re()