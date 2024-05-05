import sys, pygame
import random

pygame.init()
random.seed()  

 


screen_width = 720
screen_height = 360

windowsize = screen_width, screen_height 
black = 0, 0, 0
screen = pygame.display.set_mode(windowsize)

class StartScreen:
    def __init__(self):
        self.background = pygame.image.load("images/background.png")
        self.font = pygame.font.Font(None, 50)
        self.font_0 = pygame.font.Font(None, 80)
        self.text_1 = self.font_0.render("Welcome to My Game!", 1, (13, 15, 135))
        self.textpos_1 = self.text_1.get_rect(centerx=screen_width/2, centery=screen_height/2-140)
        self.text_2 = self.font.render("Press SPACE to start", 1, (255, 255, 255))
        self.textpos_2 = self.text_2.get_rect(centerx=screen_width/2, centery=screen_height/2 + 50)
        self.font_2 =pygame.font.Font(None,30)
        self.text_3 = self.font_2.render("press UP => speed up and press DOWN => speed down",1,(255, 255, 255))
        self.textpos_3 = self.text_2.get_rect(centerx=screen_width/2-100, centery=screen_height/2 + 100)
        self.text_4 = self.font_2.render("press [X] => + BALL and press [Z]] => - BALL",1,(255, 255, 255))
        self.textpos_4 = self.text_2.get_rect(centerx=screen_width/2-100, centery=screen_height/2 + 150)        
        self.clock = pygame.time.Clock()

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return

            screen.blit(self.background, (0, 0))
            screen.blit(self.text_1, self.textpos_1)
            screen.blit(self.text_2, self.textpos_2)
            screen.blit(self.text_3, self.textpos_3)
            screen.blit(self.text_4, self.textpos_4)
            pygame.display.flip()

            self.clock.tick(60)

class Ball:
    ball_image = pygame.image.load("images/intro_ball.gif")
    ball_rect = ball_image.get_rect()
    Clock = pygame.time.Clock()
    
    def __init__(self):
        pos = [random.random()*screen_width*0.5,random.random()*screen_height*0.5]
        r = int(random.randint(- int(screen_width / 10), int(screen_width / 10)) )
        br = Ball.ball_rect.inflate(r, r)
        self._image = pygame.transform.scale(Ball.ball_image, (br.width, br.height))
        self._ballrect = pygame.Rect(pos[0], pos[1], br.width, br.height)
        self.inter_move_time = random.randint(1, 20)
        self._direction = [1, 1]
        self.total_time_after_move = 0


    def move(self):
        self.total_time_after_move = self.total_time_after_move + Ball.Clock.get_time()
        if self.total_time_after_move <= self.inter_move_time:
            return

        self.total_time_after_move = 0

        self._ballrect = self._ballrect.move(self._direction)
        if self._ballrect.left < 0 or self._ballrect.right > screen_width:
            self._direction[0] = -self._direction[0]
        if self._ballrect.top < 0 or self._ballrect.bottom > screen_height:
            self._direction[1] = -self._direction[1]

    def speeddown(self):
        self.inter_move_time = self.inter_move_time + 1
        

    def speedup(self):
        self.inter_move_time = self.inter_move_time - 1
        
    def draw(self, screen):
        screen.blit(self._image, self._ballrect)


class Main:

    def __init__(self):
        self._paused = False
        self._ball_count = 5  
        self._balls = [Ball() for i in range(self._ball_count)]

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        for b in self._balls:
                            b.speeddown()
                    elif event.key == pygame.K_UP:
                        for b in self._balls:
                            b.speedup()
                    elif event.key == pygame.K_SPACE:
                        self._paused = not self._paused
                    elif event.key == pygame.K_r and self._paused:
                        self._paused = False
                        for b in self._balls:
                            b.speedup()
                    elif event.key == pygame.K_x:
                        self._ball_count += 1
                        if self._ball_count > len(self._balls):
                            self._balls.append(Ball())
                    elif event.key == pygame.K_z:
                        self._ball_count -= 1
                        if self._ball_count < 1:
                            self._ball_count = 1
                        if self._ball_count < len(self._balls):
                            self._balls.pop()

                  

            if not self._paused:
                screen.fill(black)
                     
                for b in self._balls:
                    b.move()
                    b.draw(screen)

                    if b.inter_move_time >= 40:
                        self._paused = True

                
                
                if self._paused:
                    font = pygame.font.Font(None, 70)
                    font_2 = pygame.font.Font(None, 30)
                    text_1 = font.render("Paused \n \n ", 1, (255, 10, 10))
                    textpos = text_1.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2)
                    text_2 = font_2.render("Increase speed and press[SPACE] or Please press[R]", 1, (255, 170, 86))
                    textpos_2 = text_1.get_rect(centerx=screen.get_width()/2-150, centery=screen.get_height()/2+50)
                    screen.blit(text_1, textpos)
                    screen.blit(text_2, textpos_2)        
                          

                pygame.display.flip()

                Ball.Clock.tick()

                



if __name__ == "__main__":
    start = StartScreen()
    start.run()
    m = Main()
    m.run()
