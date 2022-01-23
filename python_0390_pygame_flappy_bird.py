'''
Step 1) begin with main program
'''
import random
import pygame

pygame.init()

class Config:

    SCREEN_HEIGHT_ADJUST = 300

    SCREEN_LENGTH = 576
    SCREEN_HEIGHT = 1024 - SCREEN_HEIGHT_ADJUST

    BACKGROUND_X = 0
    BACKGROUND_Y = 0 - SCREEN_HEIGHT_ADJUST

    FLOOR_Y = 900 - SCREEN_HEIGHT_ADJUST

    FRAME_PER_SECOND = 120

    BIRD_GRAVTIY = 0.2

    BIRD_X = 100
    BIRD_Y = SCREEN_HEIGHT / 2

    BIRD_FLY_UP_SPEED = -8

    SCREEN = pygame.display.set_mode((SCREEN_LENGTH, SCREEN_HEIGHT))

    FONT = pygame.font.Font('python_0390_pygame_flappy_bird_font.TTF', 40)
    COLOR_WHITE = (255, 255, 255)

class Background:

    def __init__(self):
        self.background_surface = pygame.image.load('python_0390_pygame_flappy_bird_background.png').convert()
        self.background_surface = pygame.transform.scale2x(self.background_surface)

    def show(self):
        Config.SCREEN.blit(self.background_surface, (Config.BACKGROUND_X,Config.BACKGROUND_Y))


class Floor:

    def __init__(self):
        self.floor_surface = pygame.image.load('python_0390_pygame_flappy_bird_base.png').convert()
        self.floor_surface = pygame.transform.scale2x(self.floor_surface)
        self.floor_x = 0


    def show(self):
        Config.SCREEN.blit(self.floor_surface, (self.floor_x, Config.FLOOR_Y))
        self.floor_x -= 5

        if self.floor_x <= -100:
            self.floor_x = 0


class Bird:

    def __init__(self):

        # self.bird_surface = pygame.image.load("python_0390_pygame_flappy_bird_bird2.png").convert_alpha()
        # self.bird_surface = pygame.transform.scale2x(self.bird_surface)

        self.bird_surface_up = pygame.transform.scale2x(pygame.image.load("python_0390_pygame_flappy_bird_bird-upflap.png").convert_alpha())
        self.bird_surface_mid = pygame.transform.scale2x(pygame.image.load("python_0390_pygame_flappy_bird_bird-midflap.png").convert_alpha())
        self.bird_surface_down = pygame.transform.scale2x(pygame.image.load("python_0390_pygame_flappy_bird_bird-downflap.png").convert_alpha())
        self.bird_frames = [self.bird_surface_up, self.bird_surface_mid, self.bird_surface_down]
        self.bird_surface_index = 0

        self.bird_rect = self.bird_frames[self.bird_surface_index].get_rect(center=(Config.BIRD_X, Config.BIRD_Y))
        self.bird_speed_y = 0


    def show(self):
        self.bird_speed_y += Config.BIRD_GRAVTIY
        self.bird_rect.centery += self.bird_speed_y
        Config.SCREEN.blit(self.rotate(), self.bird_rect)


    def rotate(self):
        self.bird_surface_index += 1
        self.bird_surface_index %= 3
        return pygame.transform.rotozoom(self.bird_frames[self.bird_surface_index], -self.bird_speed_y * 3, 1)


    def flip_wing(self):
        self.bird_speed_y = Config.BIRD_FLY_UP_SPEED

    def check_collision(self, pipe_list):
        for pipe in pipe_list:
            if self.bird_rect.colliderect(pipe.pipe_rect):
                print('Collision')
                return True

        if self.bird_rect.bottom < 0:
            print('Fly too high!')
            return True

        if self.bird_rect.top > Config.FLOOR_Y:
            print('Fly too low!')
            return True

        return False

    def back_to_init(self):
        self.bird_speed_y = 0
        self.bird_rect.centery = Config.BIRD_Y




class Pipe:

    bottom_pipe_surface = pygame.image.load("python_0390_pygame_flappy_bird_pipe.png").convert()
    bottom_pipe_surface = pygame.transform.scale2x(bottom_pipe_surface)

    top_pipe_surface = pygame.transform.flip(bottom_pipe_surface, False, True)
    # False -> Do no flip in x direction (horizontal)
    # True -> Flip in y direction (vertical)

    CREATE_PIPE_EVENT = pygame.USEREVENT

    bottom_pipe_y_choices = [300, 400, 500]

    def __init__(self, isBottom, pipe_y):
        self.isBottom = isBottom

        if isBottom:
            self.pipe_rect = Pipe.bottom_pipe_surface.get_rect(midtop=(1700, pipe_y))
        else:
            self.pipe_rect = Pipe.top_pipe_surface.get_rect(midbottom=(1700, pipe_y))


    def show(self):
        if self.isBottom:
            Config.SCREEN.blit(Pipe.bottom_pipe_surface, self.pipe_rect)
        else:
            Config.SCREEN.blit(Pipe.top_pipe_surface, self.pipe_rect)

        self.pipe_rect.centerx -= 5

        if self.pipe_rect.centerx < 0:
            return 1
        else:
            return 0


    @classmethod
    def create_a_pair_of_pipes(cls):

        bottom_pipe_y = random.choice(Pipe.bottom_pipe_y_choices)
        top_pipe_y = bottom_pipe_y - 300

        bottom_pipe = Pipe(True, bottom_pipe_y)
        top_pipe = Pipe(False, top_pipe_y)
        return bottom_pipe, top_pipe

    @classmethod
    def start_create_pipe_timer(cls):
        pygame.time.set_timer(Pipe.CREATE_PIPE_EVENT, 1200)


class Score:

    def __init__(self):
        self.score = 0
        self.best_score = 0

    def show_score(self, score):
        self.score = score // 2
        score_surface = Config.FONT.render(str(self.score), True, Config.COLOR_WHITE)
        score_rect = score_surface.get_rect(center = (288, 100))
        Config.SCREEN.blit(score_surface, score_rect)



class FlappyBird:

    def __init__(self):
        self.background = Background()
        self.floor = Floor()
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipes = []
        self.pipes.extend(Pipe.create_a_pair_of_pipes())
        self.game_on = True
        print(f'Initial status: game_on is {self.game_on}')
        self.score = Score()


    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_on:
                        self.bird.flip_wing()
                    else:
                        self.game_on = True
                        print("User presses space bar, game restart!")
                        self.back_to_init()



            if event.type == Pipe.CREATE_PIPE_EVENT:
                self.pipes.extend(Pipe.create_a_pair_of_pipes())


    def back_to_init(self):
        self.pipes.clear()
        self.bird.back_to_init()


    def begin(self):


        Pipe.start_create_pipe_timer()

        while True:
            self.handle_events()
            self.background.show()
            self.floor.show()

            if self.game_on:
                self.bird.show()

                score = 0
                for pipe in self.pipes:
                    score += pipe.show()

                collision_happend = self.bird.check_collision(self.pipes)
                if collision_happend:
                    self.game_on = False
                    print(f"Collision happened! game status: game_on is {self.game_on}")

            self.score.show_score(score)

            pygame.display.flip()
            self.clock.tick(Config.FRAME_PER_SECOND)


if __name__ == '__main__':
    game = FlappyBird()
    game.begin()


'''
Q) How Python executes this python file? 
A) From 1st row, to last row.
Step 1) Create Config class object -> create all class variables
Step 2) Create Background class object -> does nothing extra
Step 3) Create Floor class object -> does nothing extra
Step 4) Create Bird class object -> does nothing extra
Step 5) Create Pipe class object -> create all class variables
Step 6) Create FlappyBird class object -> does nothing extra
Step 7) Start main program
Step 8) Create a FlappyBird instance object
Step 9) run FlappyBird __init__ method
Step 10) create pygame screen
   
Q) what is USER_EVENT? 
A) our developer customized event.
# Rectangle can check collision!
# The game is always in 2 state - game_on / game_over
  I use 1 single boolean variable - game_on 
  1) Initial status: game_on = True
  2) When collision happens, game_on = False
  3) When game_on is False, and when player presses the space bar, game_on = True
  
# The game should show 2 scores.
  1) score of the current game
  2) best score of all games
  
# Font 
  1) Create Font. The Font includes text style & text size.
  2) Show some text to pygame using the Font & color.
  3) The text will be put in a new surface.
  4) Put the surface in some rectangle, then you can put the rectangle wherever you'd like to put it.
   
   
'''