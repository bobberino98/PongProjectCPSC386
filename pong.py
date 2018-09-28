import pygame
from game import PongGame

pygame.init()

resolution = 800, 600

screen = pygame.display.set_mode(resolution)

pygame.display.set_caption("Pong CPSC 386")

game = PongGame(screen)

game.play()

