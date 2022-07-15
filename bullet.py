import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, game, owner, direction):
		super().__init__()
		self.screen = game.screen
		self.settings = game.settings
		self.owner = owner
		self.direction = direction

		# Bullet is a drawn rect
		self.rect = pygame.Rect(0, 0, self.owner.bullet_width, self.owner.bullet_height)
		# Bullet starting position (center of player)
		self.rect.midtop = owner.rect.center

		# Bullet's position
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)

	###TODO:
	###For the love of god, remember to refactor the projectile directions' code eventually
	# Update bullet states
	def update(self):
		# West
		if self.direction == 1:
			self.x -= self.owner.bullet_speed
		# North-west
		elif self.direction == 2:
			self.x -= self.owner.bullet_speed
			self.y -= self.owner.bullet_speed
		# North
		elif self.direction == 3:
			self.y -= self.owner.bullet_speed
		# North-east
		elif self.direction == 4:
			self.y -= self.owner.bullet_speed
			self.x += self.owner.bullet_speed
		# East
		elif self.direction == 5:
			self.x += self.owner.bullet_speed
		# South-east
		elif self.direction == 6:
			self.y += self.owner.bullet_speed
			self.x += self.owner.bullet_speed
		# South
		elif self.direction == 7:
			self.y += self.owner.bullet_speed
		# South-west
		elif self.direction == 8:
			self.y += self.owner.bullet_speed
			self.x -= self.owner.bullet_speed

		self.rect.x = self.x
		self.rect.y = self.y

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.owner.bullet_color, self.rect)
