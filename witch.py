import pygame
import random
from pygame.sprite import Sprite

class Witch(Sprite):
	def __init__(self, game):
		super().__init__()
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()

		self.image = pygame.image.load('images/witch.bmp')
		self.rect = self.image.get_rect()

		# Start position
		self.rect.midtop = self.screen_rect.midtop

		# Horizontal and Vertical positions
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Witch Info
		self.phase = 1
		self.health = 10
		self.character_speed = 60 * 0.001
		self.direction = 0

		# Witch's bullets info
		self.bullet_speed = 180 * 0.001
		self.bullet_width = 8
		self.bullet_height = 8
		self.bullet_color = (55, 113, 114)

	def _change_health(self, value):
		self.health += value

	def _invert_direction(self):
		if (self.rect.left <= 0 or self.rect.right >= self.screen_rect.right):
			self.direction *= -1

	def _reset_position(self):
		self.rect.midtop = self.screen_rect.midtop
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		if self.health <= 0:
			self.phase += 1
			self.health = self.phase*10
			self._reset_position()

		if self.direction != 0:
			# If out of bounds, it will invert positions
			self._invert_direction()

			self.x += (self.character_speed)*(self.direction)
		else:
			self.direction = 1 if (random.randint(0, 1) == 1) else -1

		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		self.screen.blit(self.image, self.rect)