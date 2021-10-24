import os
import config as cfg
import pygame
from modules import *

def main():
    pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512, devicename=None)
    pygame.init()
    screen = pygame.display.set_mode((cfg.WIDTH, cfg.HEIGHT))
    pygame.display.set_caption(cfg.TITLE)
    is_dual_mode = startInterface(screen, cfg)
    
# run
if __name__ == '__main__':
    main()