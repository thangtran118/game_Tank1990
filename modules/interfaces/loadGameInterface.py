import pygame
import sys
from itertools import cycle
from pygame.locals import *

FPS = 60

# color
#         R    G    B
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GRAY  = (192, 192, 192)


def loadGameInterface(screen, cfg, level_next=1):

    # background
    background_img = pygame.image.load(cfg.OTHER_IMAGE_PATHS.get('background'))

    # logo
    logo_img = pygame.transform.scale(pygame.image.load(cfg.OTHER_IMAGE_PATHS.get('logo')), (446, 70))
    logo_rect = logo_img.get_rect()
    logo_rect.centerx, logo_rect.centery = cfg.WIDTH//2, cfg.HEIGHT//4


    # font
    font = pygame.font.Font(cfg.FONTPATH, cfg.WIDTH//20)

    # noti loading game
    text = font.render('Loading game data, You will enter Level-%s' % level_next, True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx, text_rect.centery = cfg.WIDTH/2, cfg.HEIGHT/2

    # Loading bar
    gamebar = pygame.image.load(cfg.OTHER_IMAGE_PATHS.get('gamebar')).convert_alpha()
    gamebar_rect = gamebar.get_rect()
    gamebar_rect.centerx, gamebar_rect.centery = cfg.WIDTH/2, cfg.HEIGHT/1.4
    tank_cursor = pygame.image.load(cfg.PLAYER_TANK_IMAGE_PATHS.get('player1')[0]).convert_alpha().subsurface((0, 144), (48, 48))
    tank_rect = tank_cursor.get_rect()
    tank_rect.left, tank_rect.centery = gamebar_rect.left, gamebar_rect.centery

    # loading time 
    load_time_left = gamebar_rect.right - tank_rect.right + 8 # 8 : len of gun barrel

    fpsClock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        if load_time_left <= 0: return
        screen.blit(background_img, (0, 0))
        screen.blit(logo_img, logo_rect)
        screen.blit(text, text_rect)
        screen.blit(gamebar, gamebar_rect)
        screen.blit(tank_cursor, tank_rect)
        pygame.draw.rect(screen, GRAY, (gamebar_rect.left+8, gamebar_rect.top+8, tank_rect.left-gamebar_rect.left-8, tank_rect.bottom-gamebar_rect.top-16))
        tank_rect.left += 2
        load_time_left -= 2
        pygame.display.update()
        fpsClock.tick(FPS)
