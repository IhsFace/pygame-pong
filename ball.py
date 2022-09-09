import pygame


class Ball():
    def __init__(self, pos):
        self.pos = pos
        self.display = pygame.display.get_surface()
        self.rect = pygame.Rect(0, 0, 25, 25)
        self.rect.center = self.pos
        self.speed = pygame.math.Vector2(-8, 12)

    def move(self):
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.speed.y = self.speed.y * -1
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

    def update(self):
        self.move()
        pygame.draw.rect(self.display, (255, 255, 255), self.rect)
