import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 900))
pygame.display.set_caption("KALI THE SAUSAGE")

BG = pygame.image.load("assets/BG/Clouudy.png")

def main_menu(): #Main Menu Screen
    pygame.display.set_caption("MENU")

    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load())