import pygame
from pygame.draw import *
from random import randint

# Choose mode
# if mode = 1 will be random balls on map
# if mode = 2 will be moving balls on map
# if mode = 3 will be random and moving balls on map
mode = 2
fps = 50

def main(color_screen, fps, size_screen, mode):
    """main function in this programm

    Args:
        color_screen (list): (r, g ,b) fill screen
        fps (int): just fps
        size_screen (list): (x, y) size screen in px
        mode (str): moving_ball or random_ball
    """
    
    player_name = input('write you name \n')
    pygame.init()

    screen = pygame.display.set_mode(size_screen)
    total_scores = 0

    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    count_balls = 3
    position_balls = [(100, 100, 50)]*count_balls
    position_balls_moving = [(200, 200, 50)]*count_balls
    speed_ball = 5
    direction_balls = []
    for i in range(count_balls):
        start_x_speed = randint(1, speed_ball-1)
        start_y_speed = (speed_ball**2 - start_x_speed**2)**0.5
        direction_balls.append([start_x_speed,start_y_speed]) 


    while not finished:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    total_scores += scores(event.pos, position_balls, 5)
                    total_scores += scores(event.pos, position_balls_moving, 1)
        if mode == 1 or mode == 3:
            for i in range(count_balls):
                position_balls[i] = new_ball(screen, size_screen, 80)
        if mode == 2 or mode == 3:
            for i in range(count_balls):
                direction_balls[i] = check_direction_ball(speed_ball, direction_balls[i], position_balls_moving[i], size_screen)
                position_balls_moving[i] = moving_ball(screen, direction_balls[i], (255, 255, 255), position_balls_moving[i])
        if mode > 3:
            break

        screen.fill(color_screen)
    text_in_file(player_name, total_scores, 'scores_ex6.txt')
    pygame.quit()


def check_direction_ball(speed_ball, direction_ball, position_ball, size_screen):
    """function to correct direction of ball

    Args:
        speed_ball (int): speed ball
        direction_ball (list): speed in x and speed in y
        position_ball (list): x,y,r - position ball
        size_screen (list): widgh and height of screen (x, y)

    Returns:
        list: new direction in list format (x_speed, y_speed)
    """
    for i in range(2):
        if position_ball[i]-position_ball[2]/2 > 0:
            if position_ball[i]+position_ball[2]/2 < size_screen[i]:
                pass
            else:
                direction_ball[i] = int(-randint(0, speed_ball - 1))
                return direction_ball
        else:
            direction_ball[i] = randint(0, speed_ball)
            direction_ball[1-i] = (speed_ball**2 - direction_ball[i]**2)**0.5        
            return direction_ball
    return direction_ball


def scores(position_buttom, position_balls, multiplier):
    """function to return scores in game

    Args:
        position_buttom (list): format x and y
        position_ball (list): format x,y,r
        multiplier (int): score will be correct *multiplier
    """
    score = 0
    for position in position_balls:
        x = position_buttom[0] - position[0]
        y = position_buttom[1] - position[1]
        lenght = int((x**2 + y**2)**0.5)
        if lenght <= position[2]:
            score += 1
    return score*multiplier 


def random_color():
    """function to return random color from list
    """
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)
    COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
    return COLORS[randint(0, 5)]


def new_ball(screen, size_screen, max_radius):
    '''mode for random ball 
    return x_position, y_position, z_position'''
    x = randint(max_radius, size_screen[0])
    y = randint(max_radius, size_screen[1])
    r = randint(10, max_radius)
    circle(screen, random_color(), (x, y), r)
    pygame.display.update()
    return (x, y, r)


def moving_ball(screen, direction_ball, color, position_ball):
    """mode for moving ball

    Args:
        screen (str): using screen
        direction_ball (int): speed in px
        color (list): format (r, g, b)
        position_ball (list): format (x, y, z)
    """
    x = position_ball[0] + direction_ball[0]
    y = position_ball[1] + direction_ball[1]
    circle(screen, color, (x, y), position_ball[2])
    pygame.display.update()
    return (x, y,position_ball[2])


def text_in_file(player_name, total_score, file_name):
    """print total_score in the file

    Args:
        player_name (str): name from input()
        total_score (int): total_score of game
        file_name (str): file name
    """
    output = open(file_name, 'a')
    print('Player:', player_name, ' | Total score:', total_score, file=output)
    print('Player:', player_name)
    output.close()
    
  
main((0,0,0), fps, (900,600), mode)