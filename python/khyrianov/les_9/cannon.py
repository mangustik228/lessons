import pygame as pg
from random import randint
from pygame.constants import QUIT

def main():

    mgr = GameManager(1000, 1000)
    done = True
    clock = pg.time.Clock()     

    while done:
        clock.tick(15)
        done = mgr.processing()
        pg.display.update()
    pg.quit
    

class Cannon():
    '''make cannon in battle. health = 100
    '''
    def __init__(self, width_screen, height_screen, screen) -> None:
        print('lalala', width_screen, height_screen)
        # self.health = 100
        self.draw(width_screen, height_screen, screen)
        
    def is_alive(self):
        return self.health > 0
    
    def draw(self, width_screen, height_screen, screen):
        '''function for draw body of the tank

        Args:
            width_screen (int): width of screen
            height_screen (int): height of the screen
            screen (screen): just screen, what we init in GameManager
        '''
        x = height_screen/2
        y = int(width_screen/5*4)
        radius_whiles = 15
        count_whiles = 5
        height_cannon = 30
        width_cannon = radius_whiles*(count_whiles-1)*2
        x_whiles = int(x - (radius_whiles*2+1)*((count_whiles-1)/2))
        y_whiles = y - radius_whiles
        color = (200, 200, 200)
        color_body = (160, 210, 230)
        for i in range(5):
            pg.draw.circle(screen, color, (x_whiles + i*(radius_whiles*2+1), y_whiles), radius_whiles)     
        pg.draw.rect(screen, color_body, [x-(width_cannon/2), y-radius_whiles*1.8-height_cannon, width_cannon, height_cannon])   
           

class Target:
    pass


class Bombs:
    pass


class GameManager:
    def __init__(self, width_screen, height_screen) -> None:
        self.screen = pg.display.set_mode((width_screen, height_screen))
        self.cannon = Cannon(width_screen, height_screen, self.screen)
        
    def processing(self):
        done = True
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = False
        return done


class Shale:
    pass

main()

