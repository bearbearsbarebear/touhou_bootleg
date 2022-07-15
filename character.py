import pygame

class Character:
	def __init__(self, game):
		self.screen = game.screen
		self.screen_rect = game.screen.get_rect()

		self.image = pygame.image.load('images/character_back.bmp')
		self.rect = self.image.get_rect()

		# Start position
		self.rect.midbottom = self.screen_rect.midbottom

		# Horizontal and Vertical positions
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_north = False
		self.moving_south = False

		# Character Info
		self.health = 100
		self.character_speed = 85 * 0.001

		# Character's bullets info
		self.bullet_speed = 260 * 0.001
		self.bullet_width = 8
		self.bullet_height = 8
		self.bullet_damage = 10
		self.bullet_color = (55, 113, 114)

	# Updates character's states
	def update(self):
		# Movement updates based on flags
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.character_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.character_speed
		if self.moving_north and self.rect.top > 0:
			self.y -= self.character_speed
		if self.moving_south and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.character_speed

		# Update live position based on x and y
		self.rect.x = self.x
		self.rect.y = self.y

	# Draw image in rect
	def blitme(self):
		self.screen.blit(self.image, self.rect)
