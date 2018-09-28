import pygame


class PongGame:

    def __init__(self, screen):

        self.screen = screen

        self.screen_width = 800
        self.screen_height = 600

        self.pad_length = 100
        self.pad_speed = 10
        self.pad_width = 10
        self.ball_radius = 6

        self.lp_score = 0
        self.rp_score = 0

        self.clock = pygame.time.Clock()

        self.ball_vel_x = 5
        self.ball_vel_y = 5

        self.ball_x = 400
        self.ball_y = 300

        self.lp_pad_y = 300
        self.rp_pad_y = 300

        self.lp_move_up = False
        self.lp_move_down = False
        self.rp_move_up = False
        self.rp_move_down = False

    def draw_screen(self):
        self.screen.fill(pygame.Color(0, 0, 0, 255))
        pygame.draw.rect(self.screen, pygame.Color(128, 128, 128, 128), (self.screen_width / 2, 0, 2, self.screen_height))

    def update_ball(self):
        self.ball_x += self.ball_vel_x
        self.ball_y += self.ball_vel_y

        if self.ball_y < 0 or self.ball_y > self.screen_height - self.ball_radius:
            self.ball_vel_y *= -1
            wall_hit = pygame.mixer.Sound("sounds/wallhit.wav")
            wall_hit.play()

        if self.ball_x < 0:
            if self.lp_pad_y < self.ball_y < self.lp_pad_y + self.pad_length:
                self.ball_vel_x = -self.ball_vel_x
                paddle_hit = pygame.mixer.Sound("sounds/paddlehit.wav")
                paddle_hit.play()
            else:
                self.rp_score += 1
                self.ball_x = 400
                self.ball_y = 300
                self.ball_vel_x = 5
                self.ball_vel_y = 5
                score_sound = pygame.mixer.Sound("sounds/score.wav")
                score_sound.play()
        elif self.ball_x > self.screen_width:
            if self.rp_pad_y < self.ball_y < self.rp_pad_y + self.pad_length:
                self.ball_vel_x *= -1
                paddle_hit = pygame.mixer.Sound("sounds/paddlehit.wav")
                paddle_hit.play()
            else:
                self.lp_score += 1
                self.ball_x = 400
                self.ball_y = 300
                self.ball_vel_x = -5
                self.ball_vel_y = -5
                score_sound = pygame.mixer.Sound("sounds/score.wav")
                score_sound.play()

        pygame.draw.circle(self.screen, pygame.Color(255, 255, 255, 255), (self.ball_x, self.ball_y), self.ball_radius)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.lp_move_up = True
                    self.lp_move_down = False
                elif event.key == pygame.K_s:
                    self.lp_move_down = True
                    self.lp_move_up = False
                elif event.key == pygame.K_UP:
                    self.rp_move_up = True
                    self.rp_move_down = False
                elif event.key == pygame.K_DOWN:
                    self.rp_move_down = True
                    self.rp_move_up = False
                elif event.key == pygame.K_q:
                    exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.lp_move_up = False
                elif event.key == pygame.K_s:
                    self.lp_move_down = False
                elif event.key == pygame.K_UP:
                    self.rp_move_up = False
                elif event.key == pygame.K_DOWN:
                    self.rp_move_down = False
            elif event.type == pygame.QUIT:
                exit()

    def update_paddles(self):

        if self.lp_move_up:
            self.lp_pad_y -= self.pad_speed
            if self.lp_pad_y < 0:
                self.lp_pad_y = 0
        elif self.lp_move_down:
            self.lp_pad_y += self.pad_speed
            if self.lp_pad_y > self.screen_height - self.pad_length:
                lp_pad_y = self.screen_height - self.pad_length
        if self.rp_move_up:
            self.rp_pad_y -= self.pad_speed
            if self.rp_pad_y < 0:
                self.rp_pad_y = 0
        elif self.rp_move_down:
            self.rp_pad_y += self.pad_speed
            if self.rp_pad_y > self.screen_height - self.pad_length:
                self.rp_pad_y = self.screen_height - self.pad_length

        pygame.draw.rect(self.screen, pygame.Color(255, 255, 255, 255),
                         (0, self.lp_pad_y, self.pad_width, self.pad_length))

        pygame.draw.rect(self.screen, pygame.Color(255, 255, 255, 255),
                         (self.screen_width - self.pad_width, self.rp_pad_y, self.pad_width,
                          self.pad_length))

    def draw_scores(self):
        score_font = pygame.font.Font(None, 30)

        lp_score_text = str(self.lp_score)
        lp_score_render = score_font.render(lp_score_text, 1, pygame.Color(255, 255, 255, 255))
        self.screen.blit(lp_score_render, (self.screen_width / 2 - 50, 50))

        rp_score_text = str(self.rp_score)
        rp_score_render = score_font.render(rp_score_text, 1, pygame.Color(255, 255, 255, 255))
        self.screen.blit(rp_score_render, (self.screen_width / 2 + 50, 50))

    def play(self):
        while (True):
            pygame.mouse.set_visible(False)

            self.draw_screen()

            self.check_events()
            self.update_paddles()

            self.update_ball()
            self.draw_scores()

            pygame.display.flip()

            self.clock.tick(60)








