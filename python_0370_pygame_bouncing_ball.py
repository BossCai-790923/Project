'''
Requirement:
Our next PyGame code needs to add some animation.
Let's add a bouncing ball to the PyGame screen. And we make the ball keep on bouncing and never stop.
'''

import pygame

'''
v = gt
g = 9.8m/s^2
For free fall ball, when t0 = 0s, v0 = 0m/s
                    when t1 = 1s, v1 = 9.8m/s 
                    when t2 = 2s, v1 = 9.8 * 2 = 19.6m/s 
Here v means, velocity on y axis -> Vy.
For Vx, velocity on x axis, as there is no force on the x axis direction, Vx keeps unchanged.
Because our FPS is 100, our time unit is 0.01s
Because our distance unit is pixel, so we have to convert meter to pixel.
The ball initial velocity - [1,0]
means Vx = 1 pixel / 0.01s
      Vy = 0 pixel / 0.01s
height of my screen is about 20cm, 1080pixel
-> 5400 pixel = 100cm
-> 5400 pixel = 1m 
g=9.8m/s^2
 =9.8 * 5400 pixel / (100 * 0.01)s^2 
 =5.292 pixel / (0.01s)^2
 =5 pixel / (0.01s)^2
 
This means 
1st frame -> Vy = 0 pixel/0.01s
2nd frame (0.01s later) -> Vy = 5 pixel/0.01s
3rd frame (0.01s later) -> Vy = 10 pixel/0.01s
... 
 
'''

class Ball:

    def __init__(self, screen, screen_size, ball_file_name, ball_speed, gravity):
        self.screen = screen
        self.screen_size = screen_size
        self.ball_surface = pygame.image.load(ball_file_name)
        '''
        Q) What is surface?
        A) In pygame, we don't say image, we say surface. All images are called surface.
        '''

        self.ball_rect = self.ball_surface.get_rect()
        '''
        Q) What is rectangle?
        A) A rectangle means a rectangle on the screen. You can move it. You can merge 2 rectangles. You can check whether 2 rectangles collide with each other.
        
        Q) How to create a rectangle? 
        A) If you have a surface, you simply call surface.get_rect(), you will get a new rectangle 
        '''
        self.ball_speed = ball_speed
        # [1,1] means move by 1 pixel in x axis and 1 pixel in y axis

        self.gravity = gravity


    def check_rebounce(self):

        if self.ball_rect.left < 0:
            self.ball_rect.left = 0
            self.ball_speed[0] = -self.ball_speed[0]

        if self.ball_rect.right > self.screen_size[0]:
            self.ball_rect.right = self.screen_size[0]
            self.ball_speed[0] = -self.ball_speed[0]

        if self.ball_rect.top < 0:
            self.ball_rect.top = 0
            self.ball_speed[1] = -self.ball_speed[1]

        if self.ball_rect.bottom > self.screen_size[1]:
            self.ball_rect.bottom = self.screen_size[1]
            self.ball_speed[1] = -self.ball_speed[1]




    def show(self):

        # To let the ball start moving, we need to move the rectangle before we draw the ball in the rectangle
        # .move method will create a new rectangle, you have you assign back to self.ball_rect
        self.ball_rect = self.ball_rect.move(self.ball_speed)
        self.check_rebounce()
        self.ball_speed[1] += self.gravity
        self.screen.blit(self.ball_surface, self.ball_rect)
        '''
        Q) What's blit?
        A) In pygame, we don't say : show a image on the screen.
                      we say:        blit a surface on the screen.
        Q) Where do we blit the ball surface in the screen?
           Inside the ball rectangle
        '''


class BallGame:

    def __init__(self, framePerSecond, ball_file_name, ball_speed, screen_width, screen_height, gravity):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_size = self.screen_width, self.screen_height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.ball = Ball(self.screen, self.screen_size, ball_file_name, ball_speed, gravity)
        self.framePerSecond = framePerSecond
        self.clock = pygame.time.Clock()
        # https://www.pygame.org/docs/ref/time.html

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def draw_background(self):
        black = 0, 0, 0
        self.screen.fill(black)

    def begin(self):
        pygame.init()

        '''
        Frame Per Second (FPS) / Frame Rate (FR)
        FPS = 24 (Movie & TV show) 
        '''

        while True:
            self.handle_events()
            self.draw_background()
            self.ball.show()
            pygame.display.flip()   # flip means, refresh the screen.

            '''
            if we use 24fps, then we should finish 24 loops in 1 second.
            meaning, each loop should take exactly 1/24 second.
            meaning, after all the above 4 line of code finishes, we should make our code sleep, till 1/24 second has passed.
            '''
            self.clock.tick(self.framePerSecond)


if __name__ == '__main__':

    framePerSecond = 30

    ball_file_name = "python_0370_pygame_bouncing_ball.gif"
    # ball_file_name = "python_0370_pygame_bouncing_ball_2.png"
    # ball_file_name = "python_0370_pygame_bouncing_ball_3.png"
    # ball_file_name = "python_0370_pygame_bouncing_ball_4.png"
    # ball_file_name = "python_0370_pygame_bouncing_ball_5.png"

    # ball_speed = [1, 1]
    ball_speed = [8,1]

    # screen_width = 800
    screen_width = 1200
    screen_height = 600

    #close to modification / open the extension

    gravity = 3 # 5 pixel /0.01s^2

    game = BallGame(framePerSecond, ball_file_name, ball_speed, screen_width, screen_height, gravity)
    game.begin()