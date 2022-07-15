import pygame.font

from settings import Settings

class Text:
	def __init__(self, game, text):
		self.settings = Settings()
		self.screen = game.screen
		self.screen_rect = self.screen.get_rect()

		self.color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		self._text(text)

	def _text(self, text):
		self.text_image = self.font.render(text, True, self.color, self.settings.bg_color)
		self.text_image_rect = self.text_image.get_rect()
		self.text_image_rect.center = self.screen_rect.center

	def draw_text(self):
		self.screen.blit(self.text_image, self.text_image_rect)
