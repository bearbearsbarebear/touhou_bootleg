import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, game):
		super().__init__()
		self.screen = game.screen
		self.settings = game.settings
		self.character = game.character

		# Bullet is a drawn rect
		self.rect = pygame.Rect(0, 0, self.character.bullet_width, self.character.bullet_height)
		# Bullet starting position (above player)
		self.rect.midtop = game.character.rect.midtop

		# Bullet only walks forward, so we use it's y coordinate
		self.y = float(self.rect.y)

	# Update bullet states
	def update(self):
		self.y -= self.character.bullet_speed
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.character.bullet_color, self.rect)
