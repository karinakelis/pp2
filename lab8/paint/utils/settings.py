import pygame
pygame.init()
pygame.font.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)

FPS = 60
PIXEL_SIZE = 10
TOOLBAR_HEIGHT = 50
WIDTH,HEIGHT = 600,700

ROWS = (HEIGHT - TOOLBAR_HEIGHT) // PIXEL_SIZE
COLS = WIDTH // PIXEL_SIZE

BG_COLOR = WHITE

DRAW_GRID_LINES = True

def get_font(size):
    return pygame.font.SysFont("comicsans",size)