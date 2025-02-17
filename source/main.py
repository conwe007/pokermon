import pygame
import time
import random

FRAMERATE = 60

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pokermon")

IMAGE_BACKGROUND = pygame.image.load("./assets/background.png")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_X = 200
PLAYER_Y = WINDOW_HEIGHT - PLAYER_HEIGHT

PLAYER_VELOCITY = 5

clock = pygame.time.Clock()

player = pygame.Rect(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)

def draw():
    WINDOW.blit(IMAGE_BACKGROUND, (0, 0))

    pygame.draw.rect(WINDOW, "red", player)

    pygame.display.update()


def main():
    run = True

    while run:
        clock.tick(FRAMERATE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT]:
            player.x += PLAYER_VELOCITY
        
        draw()

    pygame.quit()

if __name__ == "__main__":
    main()

