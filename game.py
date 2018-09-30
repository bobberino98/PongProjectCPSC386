import pygame
import random
from startup import Button

class PongGame:

    def __init__(self, screen):

        self.screen = screen

        self.game_active = False
        self.screen_width = 800
        self.screen_height = 600

        self.pad_length = 100
        self.pad_speed = 10
        self.pad_width = 10
        self.ball_radius = 6

        self.p_score = 0
        self.ai_score = 0

        self.clock = pygame.time.Clock()

        self.ai_speed = 8
        self.ball_vel_x = 5
        self.ball_vel_y = 5

        self.ball_x = 400
        self.ball_y = 300

        self.ps_pad_y = 300
        self.ais_pad_y = 300
        self.ptb_pad_x = 200 - self.pad_length/2
        self.aitb_pad_x = 600 - self.pad_length/2

        self.ps_move_up = False
        self.ps_move_down = False
        self.ptb_move_left = False
        self.ptb_move_right = False
        self.start_btn = Button(self.screen, "Play")
        self.goal_score = 10
        self.ai_won = False
        self.p_won = False

    def randomize(self):
        temp = random.randint(0, 1)
        if temp == 0:
            return -1
        else:
            return 1

    def win_screen(self, winner):
        win_font = pygame.font.Font(None, 30)
        win_text = str(winner +" Wins!")
        win_render = win_font.render(win_text, 1, pygame.Color(255, 255, 255, 255))
        self.screen.blit(win_render, (self.screen_width / 2 - 50, 50))

    def draw_screen(self):
        self.screen.fill(pygame.Color(0, 0, 0, 255))
        pygame.draw.rect(self.screen, pygame.Color(128, 128, 128, 128), (self.screen_width / 2, 0, 2, self.screen_height))

    def check_play_button(self, mouse_x, mouse_y):

        button_clicked = self.start_btn.rect.collidepoint(mouse_x, mouse_y)

        if button_clicked and not self.game_active:
            pygame.mouse.set_visible(False)
            self.game_active = True

    def update_ball(self):
        self.ball_x += self.ball_vel_x
        self.ball_y += self.ball_vel_y

        if self.ball_y < 0 or self.ball_y > self.screen_height - self.ball_radius:
            if self.ball_x < self.screen_width/2:
                if self.ptb_pad_x < self.ball_x < self.ptb_pad_x + self.pad_length:
                    self.ball_vel_y = -self.ball_vel_y
                    paddle_hit = pygame.mixer.Sound("sounds/paddlehit.wav")
                    paddle_hit.play()
                elif self.ptb_pad_x < self.ball_x < self.ptb_pad_x + self.pad_length:
                    self.ball_vel_y = -self.ball_vel_y
                    paddle_hit = pygame.mixer.Sound("sounds/paddlehit.wav")
                    paddle_hit.play()
                else:
                    self.ai_score += 1
                    self.ball_x = 400
                    self.ball_y = 300
                    self.ball_vel_x = random.randint(3, 5) * self.randomize()
                    self.ball_vel_y = random.randint(3, 5) * self.randomize()
                    score_sound = pygame.mixer.Sound("sounds/score.wav")
                    score_sound.play()
                    if self.ai_score >= self.goal_score:
                        self.ai_won = True
                        self.game_active = False

            else:
                if self.aitb_pad_x < self.ball_x < self.aitb_pad_x + self.pad_length:
                    self.ball_vel_y = -self.ball_vel_y
                    paddle_hit = pygame.mixer.Sound("sounds/paddlehit.wav")
                    paddle_hit.play()
                elif self.aitb_pad_x < self.ball_x < self.aitb_pad_x + self.pad_length:
                    self.ball_vel_y = -self.ball_vel_y
                    paddle_hit = pygame.mixer.Sound("sounds/paddlehit.wav")
                    paddle_hit.play()
                else:
                    self.p_score += 1
                    self.ball_x = 400
                    self.ball_y = 300

                    self.ball_vel_x = random.randint(3, 5) * self.randomize()
                    self.ball_vel_y = random.randint(3, 5) * self.randomize()

                    score_sound = pygame.mixer.Sound("sounds/score.wav")
                    score_sound.play()
                    if self.p_score >= self.goal_score:
                        self.p_won = True
                        self.game_active = False

        if self.ball_x < 0:
            if self.ps_pad_y < self.ball_y < self.ps_pad_y + self.pad_length:
                self.ball_vel_x = -self.ball_vel_x
                paddle_hit = pygame.mixer.Sound("sounds/paddlehit.wav")
                paddle_hit.play()
            else:
                self.ai_score += 1
                self.ball_x = 400
                self.ball_y = 300
                self.ball_vel_x = 5
                self.ball_vel_y = 5
                score_sound = pygame.mixer.Sound("sounds/score.wav")
                score_sound.play()
                if self.ai_score >= self.goal_score:
                    self.ai_won = True
                    self.game_active = False
        elif self.ball_x > self.screen_width:
            if self.ais_pad_y < self.ball_y < self.ais_pad_y + self.pad_length:
                self.ball_vel_x *= -1
                paddle_hit = pygame.mixer.Sound("sounds/paddlehit.wav")
                paddle_hit.play()
            else:
                self.p_score += 1
                self.ball_x = 400
                self.ball_y = 300
                self.ball_vel_x = -5
                self.ball_vel_y = -5
                score_sound = pygame.mixer.Sound("sounds/score.wav")
                score_sound.play()
                if self.p_score >= self.goal_score:
                    self.p_won = True
                    self.game_active = False

        pygame.draw.circle(self.screen, pygame.Color(255, 255, 255, 255), (self.ball_x, self.ball_y), self.ball_radius)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.ps_move_up = True
                    self.ps_move_down = False
                elif event.key == pygame.K_s:
                    self.ps_move_down = True
                    self.ps_move_up = False
                elif event.key == pygame.K_a:
                    self.ptb_move_left = True
                    self.ptb_move_right = False

                elif event.key == pygame.K_d:
                    self.ptb_move_right = True
                    self.ptb_move_left = False

                elif event.key == pygame.K_q:
                    exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.ps_move_up = False
                elif event.key == pygame.K_s:
                    self.ps_move_down = False
                elif event.key == pygame.K_a:
                    self.ptb_move_left = False
                elif event.key == pygame.K_d:
                    self.ptb_move_right = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_play_button(mouse_x, mouse_y)

            elif event.type == pygame.QUIT:
                exit()

    def update_paddles(self):

        if self.ps_move_up:
            self.ps_pad_y -= self.pad_speed
            if self.ps_pad_y < 0:
                self.ps_pad_y = 0
        elif self.ps_move_down:
            self.ps_pad_y += self.pad_speed
            if self.ps_pad_y > self.screen_height - self.pad_length:
                self.ps_pad_y = self.screen_height - self.pad_length
        if self.ptb_move_left:
            self.ptb_pad_x -= self.pad_speed
            if self.ptb_pad_x < 0:
                self.ptb_pad_x = 0
        elif self.ptb_move_right:
            self.ptb_pad_x += self.pad_speed
            if self.ptb_pad_x > self.screen_width/2 - self.pad_length:
                self.ptb_pad_x = self.screen_width/2 - self.pad_length

        if self.ais_pad_y < self.ball_y:
            self.ais_pad_y += self.ai_speed
            if self.ais_pad_y < 0:
                self.ais_pad_y = 0
        elif self.ais_pad_y > self.ball_y:
            self.ais_pad_y -= self.ai_speed
            if self.ais_pad_y > self.screen_height - self.pad_length:
                self.ais_pad_y = self.screen_height - self.pad_length

        if self.aitb_pad_x < self.ball_x:
            self.aitb_pad_x += self.ai_speed
            if self.aitb_pad_x > self.screen_width - self.pad_length:
                self.aitb_pad_x = self.screen_width - self.pad_length
        elif self.aitb_pad_x > self.ball_x:
            self.aitb_pad_x -= self.ai_speed
            if self.aitb_pad_x < self.screen_width / 2:
                self.aitb_pad_x = self.screen_width / 2

        pygame.draw.rect(self.screen, pygame.Color(255, 255, 255, 255),
                         (0, self.ps_pad_y, self.pad_width, self.pad_length))

        pygame.draw.rect(self.screen, pygame.Color(255, 255, 255, 255),
                         (self.ptb_pad_x, 0, self.pad_length, self.pad_width))

        pygame.draw.rect(self.screen, pygame.Color(255, 255, 255, 255),
                         (self.ptb_pad_x, 600-self.pad_width, self.pad_length, self.pad_width))

        pygame.draw.rect(self.screen, pygame.Color(255, 255, 255, 255),
                         (self.aitb_pad_x, 0, self.pad_length, self.pad_width))

        pygame.draw.rect(self.screen, pygame.Color(255, 255, 255, 255),
                         (self.aitb_pad_x, 600 - self.pad_width, self.pad_length, self.pad_width))

        pygame.draw.rect(self.screen, pygame.Color(255, 255, 255, 255),
                         (self.screen_width - self.pad_width, self.ais_pad_y, self.pad_width,
                          self.pad_length))

    def draw_scores(self):
        score_font = pygame.font.Font(None, 30)

        ps_score_text = str(self.p_score)
        ps_score_render = score_font.render(ps_score_text, 1, pygame.Color(255, 255, 255, 255))
        self.screen.blit(ps_score_render, (self.screen_width / 2 - 50, 50))

        ps_win_text = str(self.goal_score)
        ps_win_render = score_font.render(ps_win_text, 1, pygame.Color(255, 255, 255, 255))
        self.screen.blit(ps_win_render, (self.screen_width / 2-10, 100))

        ais_score_text = str(self.ai_score)
        ais_score_render = score_font.render(ais_score_text, 1, pygame.Color(255, 255, 255, 255))
        self.screen.blit(ais_score_render, (self.screen_width / 2 + 50, 50))

    def play(self):
        while True:
            if self.game_active:
                pygame.mouse.set_visible(False)

                self.draw_screen()

                self.update_paddles()

                self.update_ball()
                self.draw_scores()

            elif self.ai_won:
                self.start_btn.draw_button()
                self.win_screen("CPU")
                pygame.mouse.set_visible(True)
            elif self.p_won:
                self.start_btn.draw_button()
                self.win_screen("Player")
                pygame.mouse.set_visible(True)
            else:
                self.start_btn.draw_button()

            self.check_events()



            pygame.display.flip()
            self.clock.tick(60)







