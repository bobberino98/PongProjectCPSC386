import pygame.font


class Button:

    def __init__(self, screen, msg):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 200, 50
        self.button_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(pygame.Color(0, 0, 0, 255))
        startup_font = pygame.font.Font(None, 50)
        startup_text = str("Pong -- Ai -- No Walls")
        startup_render = startup_font.render(startup_text, 1, pygame.Color(255, 255, 255, 255))
        self.screen.blit(startup_render, (800 / 2 - 100, 150))
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)