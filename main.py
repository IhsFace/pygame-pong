import pygame
import sys
from objects import Ball, Paddles


class Menu():
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        pygame.display.set_caption('Pong')
        self.window_size = pygame.math.Vector2(600, 400)
        self.display = pygame.display.set_mode(self.window_size)
        self.click = False

        self.select_sound = pygame.mixer.Sound('assets/sounds/select.wav')

    def draw_text(self, text, size, color, surface, pos):
        font = pygame.font.Font('assets/PressStart2P-Regular.ttf', size)
        text_render = font.render(text, True, color)
        text_rect = text_render.get_rect()
        text_rect.center = pos
        self.display.blit(text_render, text_rect)

    def main(self):
        while True:
            self.display.fill((0, 100, 100))

            self.draw_text('Pong', 54, (255, 255, 255),
                           self.display, (self.window_size.x // 2, 100))

            mx, my = pygame.mouse.get_pos()

            single_button = pygame.Rect(0, 0, 150, 50)
            single_button.center = (150, 300)
            if single_button.collidepoint((mx, my)):
                if self.click:
                    self.select_sound.play()
                    Main().game_state = Game().single_game()
            pygame.draw.rect(self.display, (0, 50, 50), single_button)
            pygame.draw.rect(self.display, (0, 0, 0), single_button, 5)
            self.draw_text('SINGLE', 22, (255, 255, 255),
                           self.display, single_button.center)

            multi_button = pygame.Rect(0, 0, 150, 50)
            multi_button.center = (300, 300)
            if multi_button.collidepoint((mx, my)):
                if self.click:
                    self.select_sound.play()
                    Main().game_state = Game().multi_game()
            pygame.draw.rect(self.display, (0, 50, 50), multi_button)
            pygame.draw.rect(self.display, (0, 0, 0), multi_button, 5)
            self.draw_text('MULTI', 24, (255, 255, 255),
                           self.display, multi_button.center)

            quit_button = pygame.Rect(0, 0, 150, 50)
            quit_button.center = (450, 300)
            if quit_button.collidepoint((mx, my)):
                if self.click:
                    self.select_sound.play()
                    pygame.quit()
                    sys.exit()
            pygame.draw.rect(self.display, (0, 50, 50), quit_button)
            pygame.draw.rect(self.display, (0, 0, 0), quit_button, 5)
            self.draw_text('QUIT', 24, (255, 255, 255),
                           self.display, quit_button.center)

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

            pygame.display.update()
            self.clock.tick(60)


class Game():
    def __init__(self):
        self.clock = pygame.time.Clock()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        pygame.init()
        pygame.display.set_caption('Pong')
        self.window_size = pygame.math.Vector2(600, 400)
        self.display = pygame.display.set_mode(self.window_size)
        self.click = False

        self.ball = Ball((self.window_size.x // 2, self.window_size.y // 2))
        self.paddles = Paddles()

        self.p1_score = 0
        self.p2_score = 0

        self.hit_sound = pygame.mixer.Sound('assets/sounds/hit.wav')
        self.select_sound = pygame.mixer.Sound('assets/sounds/select.wav')

    def draw_text(self, text, size, color, surface, pos):
        font = pygame.font.Font('assets/PressStart2P-Regular.ttf', size)
        text_render = font.render(text, True, color)
        text_rect = text_render.get_rect()
        text_rect.center = pos
        self.display.blit(text_render, text_rect)

    def pause(self):
        running = True
        while running:
            self.display.fill((0, 100, 100))

            self.draw_text('Paused', 36, (255, 255, 255),
                           self.display, (self.window_size.x // 2, 100))

            mx, my = pygame.mouse.get_pos()

            resume_button = pygame.Rect(0, 0, 150, 50)
            resume_button.center = (150, 300)
            if resume_button.collidepoint((mx, my)):
                if self.click:
                    self.select_sound.play()
                    running = False
            pygame.draw.rect(self.display, (0, 50, 50), resume_button)
            pygame.draw.rect(self.display, (0, 0, 0), resume_button, 5)
            self.draw_text('RESUME', 22, (255, 255, 255),
                           self.display, resume_button.center)

            menu_button = pygame.Rect(0, 0, 150, 50)
            menu_button.center = (300, 300)
            if menu_button.collidepoint((mx, my)):
                if self.click:
                    self.select_sound.play()
                    Main().game_state = Menu().main()
            pygame.draw.rect(self.display, (0, 50, 50), menu_button)
            pygame.draw.rect(self.display, (0, 0, 0), menu_button, 5)
            self.draw_text('MAIN MENU', 14, (255, 255, 255),
                           self.display, menu_button.center)

            quit_button = pygame.Rect(0, 0, 150, 50)
            quit_button.center = (450, 300)
            if quit_button.collidepoint((mx, my)):
                if self.click:
                    self.select_sound.play()
                    pygame.quit()
                    sys.exit()
            pygame.draw.rect(self.display, (0, 50, 50), quit_button)
            pygame.draw.rect(self.display, (0, 0, 0), quit_button, 5)
            self.draw_text('QUIT', 24, (255, 255, 255),
                           self.display, quit_button.center)

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
            self.clock.tick(60)

    def single_game(self):
        while True:
            self.display.fill((0, 100, 100))

            self.draw_text(f'{str(self.p1_score)} | {str(self.p2_score)}', 36, (255, 255, 255),
                           self.display, (self.window_size.x // 2, 50))

            pygame.draw.aaline(self.display, (255, 255, 255), (self.window_size.x //
                               2, 0), (self.window_size.x // 2, self.window_size.y))

            self.ball.update()
            self.paddles.update()

            if self.paddles.p2_rect.bottom > self.ball.rect.y:
                self.paddles.p2_rect.y -= self.paddles.speed + 1
            if self.paddles.p2_rect.top < self.ball.rect.y:
                self.paddles.p2_rect.y += self.paddles.speed + 1
            if self.paddles.p2_rect.y <= 0:
                self.paddles.p2_rect.y = 0
            if self.paddles.p2_rect.y >= 400:
                self.paddles.p2_rect.y = 400

            if self.ball.rect.left > self.window_size.x:
                self.p1_score += 1
                self.ball.rect.center = (
                    self.window_size.x // 2, self.window_size.y // 2)
            if self.ball.rect.right < 0:
                self.p2_score += 1
                self.ball.rect.center = (
                    self.window_size.x // 2, self.window_size.y // 2)

            if self.ball.rect.colliderect(self.paddles.p1_rect) or self.ball.rect.colliderect(self.paddles.p2_rect):
                self.hit_sound.play()
                self.ball.speed.x = self.ball.speed.x * -1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause()

            pygame.display.update()
            self.clock.tick(60)

    def multi_game(self):
        while True:
            self.display.fill((0, 100, 100))

            self.draw_text(f'{str(self.p1_score)} | {str(self.p2_score)}', 36, (255, 255, 255),
                           self.display, (self.window_size.x // 2, 50))

            pygame.draw.aaline(self.display, (255, 255, 255), (self.window_size.x //
                               2, 0), (self.window_size.x // 2, self.window_size.y))

            self.ball.update()
            self.paddles.update()
            self.paddles.p2_move()

            if self.ball.rect.left > self.window_size.x:
                self.p1_score += 1
                self.ball.rect.center = (
                    self.window_size.x // 2, self.window_size.y // 2)
            if self.ball.rect.right < 0:
                self.p2_score += 1
                self.ball.rect.center = (
                    self.window_size.x // 2, self.window_size.y // 2)

            if self.ball.rect.colliderect(self.paddles.p1_rect) or self.ball.rect.colliderect(self.paddles.p2_rect):
                self.hit_sound.play()
                self.ball.speed.x = self.ball.speed.x * -1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause()

            pygame.display.update()
            self.clock.tick(60)


class Main():
    def __init__(self):
        self.game_state = Menu().main()


if __name__ == '__main__':
    main = Main()
    main.game_state
