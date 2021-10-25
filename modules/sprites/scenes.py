import pygame

# Brick


class Brick(pygame.sprite.Sprite):
    def __init__(self, position, image_path, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

# Iron


class Iron(pygame.sprite.Sprite):
    def __init__(self, position, image_path, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

# Ice


class Ice(pygame.sprite.Sprite):
    def __init__(self, position, image_path, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((24, 24))
        for i in range(2):
            for j in range(2):
                self.image.blit(pygame.image.load(image_path), (12*i, 12*j))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

# River


class River(pygame.sprite.Sprite):
    def __init__(self, position, image_path, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((24, 24))
        for i in range(2):
            for j in range(2):
                self.image.blit(pygame.image.load(image_path), (12*i, 12*j))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position

# Tree


class Tree(pygame.sprite.Sprite):
    def __init__(self, position, image_path, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((24, 24))
        for i in range(2):
            for j in range(2):
                self.image.blit(pygame.image.load(image_path), (12*i, 12*j))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
