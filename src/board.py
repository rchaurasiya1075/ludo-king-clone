import pygame
from src.config import *

class Board:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(ASSET_IMAGE_BOARD)
        self.image = pygame.transform.scale(self.image, (BOARD_SIZE, BOARD_SIZE))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        
        # This would be a pre-calculated list of (x, y) coordinates for each cell on the path.
        # This is CRUCIAL for token movement. You can define it manually or calculate it.
        self.cell_positions = [
            (500, 650), (500, 600), (500, 550), # ... for all 52 cells
            # and 6 cells for each home column
        ]

    def draw(self):
        self.screen.blit(self.image, self.rect)
