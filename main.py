import config as cfg
import pygame
from modules import *

def main():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
    pygame.init()
    screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
    pygame.display.set_caption(cfg.TITLE)
    sounds = {}
    for key, value in cfg.AUDIO_PATHS.items():
        sounds[key] = pygame.mixer.Sound(value)
        sounds[key].set_volume(1)
    is_dual_mode = startInterface(screen, cfg)
    levelfilepaths = cfg.LEVELFILEPATHS
    for idx, levelfilepath in enumerate(levelfilepaths):
        loadGameInterface(screen, cfg, idx+1)
        game = Game(idx+1, levelfilepath, sounds, is_dual_mode, cfg)
        is_win = game.start(screen)
        if not is_win: break
    is_quit_game = endInterface(screen, cfg, is_win)
    return is_quit_game
    
# run
if __name__ == '__main__':
    while True:
        is_quit_game = main()
        if is_quit_game:
            break