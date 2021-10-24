import pygame
import sys
from itertools import cycle
from pygame.locals import *

BLINK_EVENT = pygame.USEREVENT + 0

FPS = 60

# color
#         R    G    B
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GRAY  = (192, 192, 192)

def startInterface(screen, cfg):

    #background
    background_img = pygame.image.load(cfg.OTHER_IMAGE_PATHS.get('background'))

    # logo 
    logo_img = pygame.transform.scale(pygame.image.load(cfg.OTHER_IMAGE_PATHS.get('logo')), (446, 70))
    logo_rect = logo_img.get_rect()
    logo_rect.centerx, logo_rect.centery = cfg.WIDTH//2, cfg.HEIGHT//4

    # tank cursor
    tank_cursor = pygame.image.load(cfg.PLAYER_TANK_IMAGE_PATHS.get('player1')[0]).convert_alpha().subsurface((0, 144), (48, 48))
    tank_rect = tank_cursor.get_rect()
    
    #font
    font = pygame.font.Font(cfg.FONTPATH, cfg.WIDTH//12)

    # user's choice
    one_player_white = font.render('1 PLAYER', True, WHITE)
    one_player_red = font.render('1 PLAYER', True, RED)
    one_player_rect = one_player_white.get_rect()
    one_player_rect.left, one_player_rect.top = cfg.WIDTH/2.8, cfg.HEIGHT/2.5
    two_players_white = font.render('2 PLAYERS', True, WHITE)
    two_players_red = font.render('2 PLAYERS', True, RED)
    two_players_rect = two_players_white.get_rect()
    two_players_rect.left, two_players_rect.top = cfg.WIDTH/2.8, cfg.HEIGHT/2    

    # blink text : " press ... " 
    # I copied it in stackoverflow
    # But I don't understand how to do that
    
    game_tip = font.render('press <Enter> to start', True, WHITE)
    game_tip_rect = game_tip.get_rect()
    game_tip_rect.centerx, game_tip_rect.top = cfg.WIDTH/2, cfg.HEIGHT/1.4
    game_tip_surfaces = cycle([game_tip, pygame.Surface(game_tip_rect.size)])
    game_tip_surface = next(game_tip_surfaces)
    pygame.time.set_timer(BLINK_EVENT, 600)
    fpsClock = pygame.time.Clock()
    is_dual_mode = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == BLINK_EVENT:
                game_tip_surface = next(game_tip_surfaces)
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_RETURN:
                    return is_dual_mode
                elif event.key == K_UP or event.key == K_DOWN or event.key == K_w == event.key == K_s:
                    is_dual_mode = not is_dual_mode 
        screen.blit(background_img, (0,0))
        screen.blit(logo_img, logo_rect)
        screen.blit(game_tip_surface, game_tip_rect)
        if is_dual_mode:
            tank_rect.right, tank_rect.top = two_players_rect.left - 10, two_players_rect.top 
            screen.blit(tank_cursor, tank_rect)
            screen.blit(one_player_white, one_player_rect)
            screen.blit(two_players_red, two_players_rect)
        else:
            tank_rect.right, tank_rect.top = one_player_rect.left - 10, one_player_rect.top 
            screen.blit(tank_cursor, tank_rect)
            screen.blit(one_player_red, one_player_rect)
            screen.blit(two_players_white, two_players_rect)

        pygame.display.update()
        fpsClock.tick(FPS)