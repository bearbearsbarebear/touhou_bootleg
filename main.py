import sys
import pygame
import time

from settings import Settings
from character import Character
from bullet import Bullet
from witch import Witch
from text import Text

class TouhouBootleg:
	def __init__(self):
		pygame.init()

		# Initialize Settings
		self.settings = Settings()

		# Start the game inactive
		self.game_state = False

		# Initialize Screen
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption(self.settings.title)

		pygame.mouse.set_visible(False)

		# Initialize Character
		self.character = Character(self)
		# Initialize Drawn Bullets
		self.bullets = pygame.sprite.Group()
		# Initialize Witch
		self.witch = Witch(self)

		# Start Text
		self.start_text = Text(self, "Press F5 to start")

	def run_game(self):
		# Game's main loop
		while True:
			self._check_events()

			if self.game_state:
				self.character.update()
				self.witch.update()
				self._update_bullets()

			self._update_screen()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._keyup_events(event)

	def _keydown_events(self, event):
		if event.key == pygame.K_F5:
			self.game_state = True

		if self.game_state == True:
			if event.key == pygame.K_d:
				self.character.moving_right = True
			if event.key == pygame.K_a:
				self.character.moving_left = True
			if event.key == pygame.K_w:
				self.character.moving_north = True
			if event.key == pygame.K_s:
				self.character.moving_south = True
			if event.key == pygame.K_SPACE:
				self._fire_bullet()

	def _keyup_events(self, event):
		if event.key == pygame.K_d:
			self.character.moving_right = False
		if event.key == pygame.K_a:
			self.character.moving_left = False
		if event.key == pygame.K_w:
			self.character.moving_north = False
		if event.key == pygame.K_s:
			self.character.moving_south = False

	def _fire_bullet(self):
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	def _update_bullets(self):
		self.bullets.update()

		for bullet in self.bullets.copy():
			self._check_collisions(bullet)
			self._check_out_of_bound(bullet)

	def _check_collisions(self, bullet):
		collision = bullet.rect.colliderect(self.witch.rect)
		if collision:
			self.witch._change_health(-self.character.bullet_damage)
			self.bullets.remove(bullet)

	def _check_out_of_bound(self, bullet):
		if bullet.rect.bottom <= 0:
			self.bullets.remove(bullet)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.character.blitme()
		self.witch.blitme()

		if not self.game_state:
			self.start_text.draw_text()

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		pygame.display.flip()

if __name__ == '__main__':
	game = TouhouBootleg()
	game.run_game()