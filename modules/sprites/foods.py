import pygame
import random

# used to receive items
class Foods(pygame.sprite.Sprite):
    def __init__(self, food_image_paths, screensize, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.name = random.choice(list(food_image_paths.keys()))
        self.image = pygame.image.load(food_image_paths.get(self.name))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = random.randint(100, screensize[0]-100), random.randint(100, screensize[1]-100)
        self.exist_time = 1000
    def update(self):
        self.exist_time -= 1
        return True if self.exist_time < 0 else False