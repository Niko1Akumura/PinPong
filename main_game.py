import pygame
import sys
from menu import menu

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
KHAKI = (240, 230, 140)
BALL = (154, 205, 50)
GAMEOVER = (139, 0, 0)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 60)

    def move(self, speed):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= speed
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT:
            self.rect.y += speed

    def draw(self):
        pygame.draw.rect(screen, KHAKI, self.rect)

class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.speed = [3, 3]

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed[1] = -self.speed[1]

        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            game_over()

    def draw(self):
        pygame.draw.rect(screen, BALL, self.rect)

def game_over():
    global menu_mode
    font = pygame.font.Font(None, 55)
    text = font.render("Game Over", True, GAMEOVER)
    text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)
    menu()

background = pygame.image.load('img/bg.png')
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ping Pong")

icon = pygame.image.load('img/icon.jpeg')  
pygame.display.set_icon(icon)

ping_paddle_left = Paddle(10, WINDOW_HEIGHT // 2 - 30)
ping_paddle_right = Paddle(WINDOW_WIDTH - 20, WINDOW_HEIGHT // 2 - 30)
ping_ball = Ball(WINDOW_WIDTH // 2 - 5, WINDOW_HEIGHT // 2 - 5)

clock = pygame.time.Clock()

g_score = 0

FONT = pygame.font.Font(None, 36)

win_image = pygame.image.load('img/win.gif')
win_image = pygame.transform.scale(win_image, (250, 150))
win_sound = pygame.mixer.Sound('audio/win.wav')

def main_game():
    clock = pygame.time.Clock()
    g_score = 0
    FONT = pygame.font.Font(None, 36)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ping_paddle_left.move(5)
        ping_paddle_right.move(5)
        ping_ball.move()

        if ping_ball.rect.colliderect(ping_paddle_left.rect) or ping_ball.rect.colliderect(ping_paddle_right.rect):
            ping_ball.speed[0] = -ping_ball.speed[0]
            g_score += 1 

        screen.blit(background, (0, 0))

        ping_paddle_left.draw()
        ping_paddle_right.draw()
        ping_ball.draw()

        score_text = FONT.render(f"Счёт: {g_score}", True, (255, 255, 255))
        screen.blit(score_text, (WINDOW_WIDTH - score_text.get_width() - 10, 10))

        if g_score == 200:
            win_rect = win_image.get_rect()
            win_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
            screen.blit(win_image, win_rect)
            win_sound.play()
            pygame.display.flip()
            pygame.time.delay(3000)
            game_over()

        pygame.display.flip()
        clock.tick(60)

def run_game():
    while True:
        choice = menu()
        if choice == "play":
            main_game()

run_game()