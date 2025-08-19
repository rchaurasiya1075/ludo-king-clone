import pygame
import sys
from src.config import *
from src.board import Board
from src.dice import Dice
from src.player import Player

class LudoGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Ludo Champion")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Game Objects
        self.board = Board(self.screen)
        self.players = [
            Player("red", (50, 50)), # Color and some screen position hint
            Player("green", (50, SCREEN_HEIGHT - 150)),
            # ... add yellow and blue
        ]
        self.current_player_idx = 0
        self.dice = Dice(self.screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.dice_value = None
        self.rolled_this_turn = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.rolled_this_turn:
                    self.dice_value = self.dice.roll()
                    self.rolled_this_turn = True
                    print(f"Rolled a {self.dice_value}")
                    # TODO: Logic to find movable tokens
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # Left click
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if dice was clicked
                    if self.dice.rect.collidepoint(mouse_pos) and not self.rolled_this_turn:
                        self.dice_value = self.dice.roll()
                        self.rolled_this_turn = True
                    # Check if a token was clicked (if roll happened)
                    if self.rolled_this_turn:
                        current_player = self.players[self.current_player_idx]
                        for token in current_player.tokens:
                            if token.rect.collidepoint(mouse_pos):
                                if token.can_move(self.dice_value, self.board):
                                    token.move(self.dice_value, self.board)
                                    # TODO: Handle captures, next turn logic
                                    self.next_turn()

    def next_turn(self):
        # If you didn't roll a 6, move to the next player
        if self.dice_value != 6:
            self.current_player_idx = (self.current_player_idx + 1) % len(self.players)
        self.rolled_this_turn = False
        self.dice_value = None

    def update(self):
        # Update game state, animations, etc.
        self.dice.update() # If dice has a rolling animation

    def render(self):
        self.screen.fill(LIGHT_GREY)
        self.board.draw()
        for player in self.players:
            player.draw(self.screen)
        self.dice.draw(self.screen)
        # Draw UI text (current player, dice value)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = LudoGame()
    game.run()
