import pygame
import sys
from itertools import cycle
from pygame.locals import *

BLINK_EVENT = pygame.USEREVENT + 0

FPS = 60

# color
#         R    G    B
WHITE = (255, 255, 255)
RED =   (255,   0,   0)
GRAY =  (192, 192, 192)


def endInterface(screen, cfg, is_win = False):

    # background
    background_img = pygame.image.load(cfg.OTHER_IMAGE_PATHS.get('background'))

    # font
    font = pygame.font.Font(cfg.FONTPATH, cfg.WIDTH//12)

    # blink image : " game over" 
    # I copied it in stackoverflow
    # But I don't understand how to do that
    
    gameover_img = pygame.transform.scale(pygame.image.load(cfg.OTHER_IMAGE_PATHS.get('gameover')), (150, 75))
    gameover_img_rect = gameover_img.get_rect()
    gameover_img_rect.midtop = cfg.WIDTH/2, cfg.HEIGHT/8
    gameover_img_surfaces = cycle([gameover_img, pygame.Surface(gameover_img_rect.size)])
    gameover_img_surface = next(gameover_img_surfaces)
    pygame.time.set_timer(BLINK_EVENT, 600)

    # win interface
    if is_win:
        text = font.render('Congratulations, You win!', True, WHITE)
    else:
        text = font.render('Sorry, You fail!', True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx, text_rect.centery = cfg.WIDTH/2, cfg.HEIGHT/3

    # Restart or quit
    tank_cursor = pygame.image.load(cfg.PLAYER_TANK_IMAGE_PATHS.get('player1')[0]).convert_alpha().subsurface((0, 144), (48, 48))
    tank_rect = tank_cursor.get_rect()
    restart_render_white = font.render('RESTART', True, WHITE)
    restart_render_red = font.render('RESTART', True, RED)
    restart_rect = restart_render_white.get_rect()
    restart_rect.left, restart_rect.top = cfg.WIDTH/2.4, cfg.HEIGHT/2
    quit_render_white = font.render('QUIT', True, WHITE)
    quit_render_red = font.render('QUIT', True, RED)
    quit_rect = quit_render_white.get_rect()
    quit_rect.left, quit_rect.top = cfg.WIDTH/2.4, cfg.HEIGHT/1.6
    is_quit_game = False
    
    fpsClock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == BLINK_EVENT:
                gameover_img_surface = next(gameover_img_surfaces)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_RETURN:
                    return is_quit_game
                elif event.key == K_UP or event.key == K_DOWN or event.key == K_w == event.key == K_s:
                    is_quit_game = not is_quit_game
        screen.blit(background_img, (0, 0))
        screen.blit(gameover_img_surface, gameover_img_rect)
        screen.blit(text, text_rect)
        if not is_quit_game:
            tank_rect.right, tank_rect.top = restart_rect.left-10, restart_rect.top
            screen.blit(tank_cursor, tank_rect)
            screen.blit(restart_render_red, restart_rect)
            screen.blit(quit_render_white, quit_rect)
        else:
            tank_rect.right, tank_rect.top = quit_rect.left-10, quit_rect.top
            screen.blit(tank_cursor, tank_rect)
            screen.blit(restart_render_white, restart_rect)
            screen.blit(quit_render_red, quit_rect)
        pygame.display.update()
        fpsClock.tick(FPS)
