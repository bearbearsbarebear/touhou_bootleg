import pygame
import random
import time
from pygame.sprite import Sprite

class Witch(Sprite):
	def __init__(self, game):
		super().__init__()
		self.game = game
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
		self.name = "Red Witch"
		self.phase = 1
		self.health = 10
		self.character_speed = 60 * 0.001
		self.direction = 0
		self.fire_rate = 1000
		self.attack_cooldown = 0
		self.action_events = []

		# Witch's bullets info
		self.bullet_speed = 200 * 0.001
		self.bullet_width = 12
		self.bullet_height = 12
		self.bullet_damage = 10
		self.bullet_color = (136, 0, 21)

	# Changes health by value
	def _change_health(self, value):
		self.health += value

	# Invert the direction the witch is walking
	def _invert_direction(self):
		if (self.rect.left <= 0 or self.rect.right >= self.screen_rect.right):
			self.direction *= -1

	# Centers the witch's position
	def _reset_position(self):
		self.rect.midtop = self.screen_rect.midtop
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def _vertical_walking(self):
		if self.direction != 0:
			# If out of bounds, it will invert positions
			self._invert_direction()

			self.x += (self.character_speed)*(self.direction)
		else:
			self.direction = 1 if (random.randint(0, 1) == 1) else -1

	def _phase_events(self):
		time_ms = round(time.time() * 1000)

		# Movement for each phase
		if self.phase == 1:
			self._vertical_walking()
			if self.attack_cooldown <= time_ms:
				self._add_event("attack", 7, time_ms)
				self._add_event("attack", 7, time_ms+50)
				self._add_event("attack", 7, time_ms+100)
				self._add_event("attack", 7, time_ms+150)
				self._add_event("attack", 7, time_ms+200)
				self._add_event("attack", 7, time_ms+250)
				self._add_event("attack", 7, time_ms+300)
				self.attack_cooldown = time_ms + self.fire_rate
		elif self.phase == 2:
			self._vertical_walking()
		elif self.phase == 3:
			self._vertical_walking()
		elif self.phase == 4:
			self._vertical_walking()
		elif self.phase == 5:
			self._vertical_walking()

	def _add_event(self, etype, info, time):
		event = {
			"type": etype,
			"info": info,
			"time": time
		}
		self.action_events.append(event)

	def _execute_events(self):
		time_ms = round(time.time() * 1000)

		for event in self.action_events:
			if event["time"] <= time_ms:
				if event["type"] == "attack":
					self.game._fire_bullet(self, event["info"])
				print("Event popped:", event)
				self.action_events.remove(event)

	# "Main loop" of the witch's movements, this is called in TouhouBootleg.run_game() at main.py
	def update(self):
		# Whenever health is depleted, changes phase and resets witch's position
		# If phase is 5 the game is supposed to end
		if self.health <= 0:
			if self.phase != 5:
				self.phase += 1
				self.health = self.phase*10 + 20
				self._reset_position()
			else:
				return print("Game is supposed to end")

		self._phase_events()
		self._execute_events()

		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		self.screen.blit(self.image, self.rect)