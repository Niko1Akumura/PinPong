import pygame
import sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 600, 400
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

icon = pygame.image.load('img/icon.jpeg')
pygame.display.set_icon(icon)
pygame.display.set_caption("Menu")

menu_background = pygame.image.load('img/menu.png')
menu_background = pygame.transform.scale(menu_background, (WINDOW_WIDTH, WINDOW_HEIGHT))

button_spacing = 100 

def draw_menu():
    menu_font = pygame.font.Font(None, 36)
    play_text = menu_font.render("Играть", True, (255, 255, 255))
    exit_text = menu_font.render("Выйти", True, (255, 255, 255))

    play_rect = play_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - button_spacing // 2))
    exit_rect = exit_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + button_spacing // 2))

    screen.blit(menu_background, (0, 0))

    screen.blit(play_text, play_rect)
    screen.blit(exit_text, exit_rect)

    return play_rect, exit_rect

def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    return "play"
                elif exit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        screen.fill((0, 0, 0))

        play_button, exit_button = draw_menu()

        pygame.display.flip()

menu()
