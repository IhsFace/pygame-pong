import pygame
import sys
from ball import Ball
from paddles import Paddles


def draw_text(text, size, color, surface, pos):
    font = pygame.font.Font('assets/PressStart2P-Regular.ttf', size)
    text_render = font.render(text, True, color)
    text_rect = text_render.get_rect()
    text_rect.center = pos
    display.blit(text_render, text_rect)


def main_menu():
    while True:
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        display.fill((0, 100, 100))

        draw_text('Pong', 54, (255, 255, 255),
                  display, (window_size.x // 2, 100))

        mx, my = pygame.mouse.get_pos()

        single_button = pygame.Rect(0, 0, 150, 50)
        single_button.center = (150, 300)
        if single_button.collidepoint((mx, my)):
            if click:
                select_sound.play()
                game_state = single_game()
        pygame.draw.rect(display, (0, 50, 50), single_button)
        pygame.draw.rect(display, (0, 0, 0), single_button, 5)
        draw_text('SINGLE', 22, (255, 255, 255), display, single_button.center)

        multi_button = pygame.Rect(0, 0, 150, 50)
        multi_button.center = (300, 300)
        if multi_button.collidepoint((mx, my)):
            if click:
                select_sound.play()
                game_state = multi_game()
        pygame.draw.rect(display, (0, 50, 50), multi_button)
        pygame.draw.rect(display, (0, 0, 0), multi_button, 5)
        draw_text('MULTI', 24, (255, 255, 255), display, multi_button.center)

        quit_button = pygame.Rect(0, 0, 150, 50)
        quit_button.center = (450, 300)
        if quit_button.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.quit()
                sys.exit()
        pygame.draw.rect(display, (0, 50, 50), quit_button)
        pygame.draw.rect(display, (0, 0, 0), quit_button, 5)
        draw_text('QUIT', 24, (255, 255, 255), display, quit_button.center)

        pygame.display.update()
        clock.tick(60)


def pause():
    running = True
    while running:
        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        display.fill((0, 100, 100))

        draw_text('Paused', 36, (255, 255, 255),
                  display, (window_size.x // 2, 100))

        mx, my = pygame.mouse.get_pos()

        resume_button = pygame.Rect(0, 0, 150, 50)
        resume_button.center = (150, 300)
        if resume_button.collidepoint((mx, my)):
            if click:
                select_sound.play()
                running = False
        pygame.draw.rect(display, (0, 50, 50), resume_button)
        pygame.draw.rect(display, (0, 0, 0), resume_button, 5)
        draw_text('RESUME', 22, (255, 255, 255), display, resume_button.center)

        menu_button = pygame.Rect(0, 0, 150, 50)
        menu_button.center = (300, 300)
        if menu_button.collidepoint((mx, my)):
            if click:
                select_sound.play()
                game_state = main_menu()
        pygame.draw.rect(display, (0, 50, 50), menu_button)
        pygame.draw.rect(display, (0, 0, 0), menu_button, 5)
        draw_text('MAIN MENU', 14, (255, 255, 255),
                  display, menu_button.center)

        quit_button = pygame.Rect(0, 0, 150, 50)
        quit_button.center = (450, 300)
        if quit_button.collidepoint((mx, my)):
            if click:
                select_sound.play()
                pygame.quit()
                sys.exit()
        pygame.draw.rect(display, (0, 50, 50), quit_button)
        pygame.draw.rect(display, (0, 0, 0), quit_button, 5)
        draw_text('QUIT', 24, (255, 255, 255), display, quit_button.center)

        pygame.display.update()
        clock.tick(60)


def single_game():
    p1_score = 0
    p2_score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

        display.fill((0, 100, 100))

        draw_text(f'{str(p1_score)} | {str(p2_score)}', 36,
                  (255, 255, 255), display, (window_size.x // 2, 50))

        pygame.draw.aaline(display, (255, 255, 255), (window_size.x //
                           2, 0), (window_size.x // 2, window_size.y))

        ball.update()
        paddles.update()

        if paddles.p2_rect.bottom > ball.rect.y:
            paddles.p2_rect.y -= paddles.speed + 5
        if paddles.p2_rect.top < ball.rect.y:
            paddles.p2_rect.y += paddles.speed + 5
        if paddles.p2_rect.y <= 0:
            paddles.p2_rect.y = 0
        if paddles.p2_rect.y >= 400:
            paddles.p2_rect.y = 400

        if ball.rect.left > window_size.x:
            p1_score += 1
            ball.rect.center = (
                window_size.x // 2, window_size.y // 2)
        if ball.rect.right < 0:
            p2_score += 1
            ball.rect.center = (
                window_size.x // 2, window_size.y // 2)

        if ball.rect.colliderect(paddles.p1_rect) or ball.rect.colliderect(paddles.p2_rect):
            hit_sound.play()
            ball.speed.x = ball.speed.x * -1

        pygame.display.update()
        clock.tick(60)


def multi_game():
    p1_score = 0
    p2_score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()

        display.fill((0, 100, 100))

        draw_text(f'{str(p1_score)} | {str(p2_score)}', 36,
                  (255, 255, 255), display, (window_size.x // 2, 50))

        pygame.draw.aaline(display, (255, 255, 255), (window_size.x //
                           2, 0), (window_size.x // 2, window_size.y))

        ball.update()
        paddles.update()
        paddles.p2_move()

        if ball.rect.left > window_size.x:
            p1_score += 1
            ball.rect.center = (
                window_size.x // 2, window_size.y // 2)
        if ball.rect.right < 0:
            p2_score += 1
            ball.rect.center = (
                window_size.x // 2, window_size.y // 2)

        if ball.rect.colliderect(paddles.p1_rect) or ball.rect.colliderect(paddles.p2_rect):
            hit_sound.play()
            ball.speed.x = ball.speed.x * -1

        pygame.display.update()
        clock.tick(60)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.display.set_caption('Pong')
window_size = pygame.math.Vector2(600, 400)
display = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

ball = Ball((window_size.x // 2, window_size.y // 2))
paddles = Paddles()

hit_sound = pygame.mixer.Sound('assets/sounds/hit.wav')
select_sound = pygame.mixer.Sound('assets/sounds/select.wav')

if __name__ == '__main__':
    game_state = main_menu()
