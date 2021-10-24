import pygame, sys

sys.path.append("../..")
import config as cfg

FPS = 60

# color
#         R    G    B
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GRAY  = (192, 192, 192)

background_img = pygame.image.load(cfg.OTHER_IMAGE_PATHS.get('background'))



