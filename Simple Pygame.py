#------------------------------------------------
#Dylan Friesen
#Simple Pygame
#Nov.19 2019
#------------------------------------------------

#------------------Imports--------------------
import pygame, random, time

#----------------Classes/Defs----------------

WIDTH = 1000
HEIGHT = 800
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Circle():
    
    def __init__(self, colour): #setting the parameters for self
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(20,80)
        self.colour = colour
        
    def move(self):
        self.move_x = random.randrange(-4,8)
        self.move_y = random.randrange(-4,8)
        self.x += self.move_x
        self.y += self.move_y
        
        if self.x < 0: self.x = 0
        elif self.x > WIDTH: self.x = WIDTH
        
        if self.y < 0: self.y = 0
        elif self.y > HEIGHT: self.y = HEIGHT
            
def background(circle):
    game_display.fill(WHITE)
    pygame.draw.circle(game_display, circle.colour, [circle.x, circle.y], circle.size)
    circle.move()
    pygame.display.update()
    
def main():
    green_circle = Circle(GREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        background(green_circle)
        clock.tick(60)
        
if __name__ == '__main__':
    main()
        
        
    
