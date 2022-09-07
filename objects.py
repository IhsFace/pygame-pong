import pygame


class Ball():
    def __init__(self, pos):
        self.pos = pos
        self.display = pygame.display.get_surface()
        self.rect = pygame.Rect(0, 0, 25, 25)
        self.rect.center = self.pos
        self.speed = pygame.math.Vector2(-4, 6)

    def move(self):
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.speed.y = self.speed.y * -1
        self.rect.x += self.speed.x
        self.rect.y += self.speed.y

    def update(self):
        self.move()
        pygame.draw.rect(self.display, (255, 255, 255), self.rect)


class Paddles():
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.speed = 5

        self.p1_rect = pygame.Rect(0, 0, 5, 75)
        self.p1_rect.center = (0, 200)
        self.p1_rect.left = 0

        self.p2_rect = pygame.Rect(0, 0, 5, 75)
        self.p2_rect.center = (0, 200)
        self.p2_rect.right = 600

    def p1_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.p1_rect.y -= self.speed
        if keys[pygame.K_s]:
            self.p1_rect.y += self.speed
        if self.p1_rect.top <= 0:
            self.p1_rect.top = 0
        if self.p1_rect.bottom >= 400:
            self.p1_rect.bottom = 400

    def p2_move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.p2_rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.p2_rect.y += self.speed
        if self.p2_rect.top <= 0:
            self.p2_rect.top = 0
        if self.p2_rect.bottom >= 400:
            self.p2_rect.bottom = 400

    def update(self):
        self.p1_move()
        pygame.draw.rect(self.display, (255, 255, 255), self.p1_rect)
        pygame.draw.rect(self.display, (255, 255, 255), self.p2_rect)
