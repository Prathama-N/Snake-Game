import pygame
import time
import random
import pygame, sys
from pygame.locals import *

print('\n:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-WELCOME-:-:-:-TO-:-:-:-SNAKE-:-:-:-GAME-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:')

#instructions
print('\n=============INSTRUCTIONS  AND  DIRECTIONS=============\n',
      '1. Use ↑ (arrow up key) to go in UP direction.'
      '\n2. Use ↓ (arrow down key) to go in DOWN direction.'
      '\n3. Use ← (left arrow key) to go in LEFT direction.'
      '\n4. Use → (right arrow key) to go in RIGHT directioon.'
      '\n5. Use SPACE bar to pause and unpause the game.'
      '\n6. Please Enter Your name and colours for food and snake.')

#inputs given users
print('\n:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-LET''S  START  THE  GAME:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-\n')
name=input('\nEnter your name:  ')
print('\nAvailable colours are:  WHITE, BLUE, BROWN, CYAN, YELLOW, RED, GREEN, VIOLET, ORANGE, MAGENTA ')
a=input('\nEnter the snake colour for your first hunt: ')
b=input('Enter the food colour for your first hunt:')
c=input('\nEnter the snake colour after your first hunt: ')
d=input('Enter the food colour after your first hunt: ')

#snake size and speed
snake_speed = 7
snake_x=45
snake_y=55
snk_list =[]
snk_length = 1

# Window size
window_x = 1020
window_y = 500

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
brown=pygame.Color(255, 64, 64)
cyan=pygame.Color(0, 238, 238)
yellow=pygame.Color(255,255,0)
violet=pygame.Color(138,43,226)
orange=pygame.Color(255,97,3)
magenta=pygame.Color(255,0,255)

# Initialising pygame
pygame.init()
 
# Initialise game window
pygame.display.set_caption('Snake game')
game_window = pygame.display.set_mode((window_x, window_y))


#Add music
pygame.mixer.music.load("Snake Game - Theme Song.mp3")
pygame.mixer.music.play(-1)

 
# FPS (frames per second) controller
fps = pygame.time.Clock()
 
# defining snake default position
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                  random.randrange(1, (window_y//10)) * 10]
 
fruit_spawn = True
 
# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
with open("hiscore.txt", "r") as f:
        hiscore = f.read()

 
# displaying Score function
def show_score(choice, color, font, size):

    with open("hiscore.txt","r") as f:
        hiscore=f.read()

    if score>int(hiscore):
            hiscore=score
   
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)
     
    # create the display surface object
    # score_surface
    score_surface = score_font.render('Name: '+str(name)+'                   '+'Your Score is : '
                                      + str(score)+ '             '+'Hiscore: '+str(hiscore)+'           '+'Press space bar to PAUSE and esc key to QUIT GAME', True, color)
    
    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
     
    # displaying text
    game_window.blit(score_surface, score_rect)

#pausing the game  
def pause():
    loop = 1
    my_font = pygame.font.SysFont('times new roman', 50)

    game_over_surface = my_font.render('PAUSED:', True, red)
    game_over_surface = my_font.render('Press Space to continue', True, white)
    pause_rect = game_over_surface.get_rect(center=(window_x/2,window_y/2))
    #pause_rect = game_over_surface.get_rect()

    game_window.blit(game_over_surface, pause_rect)

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    loop = 0
                if event.key == pygame.K_SPACE:
                    game_window.fill((0,0,0))
                    loop = 0
        pygame.display.update()
        
        clock.tick(60)

    pause_rect = game_over_surface.get_rect()

    game_window.blit(game_over_surface, pause_rect)


        
 
# game over function
def game_over():
    with open("hiscore.txt","w") as f:
        f.write(str(hiscore))
   # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 30)

    # creating a text surface on which text will be drawn
    if score>=int(hiscore):
        game_over_surface = my_font.render('Congratulations  '+str(name)+'!!!'+'          '+'Your Score is : ' + str(score)+ '         '+' Hiscore: '+str(hiscore), True, red)
    else:
        game_over_surface = my_font.render('Better Luck Next Time'+str(name)+'!!!'+'          '+'Your Score is : ' + str(score)+ '         '+' Hiscore: '+str(hiscore), True, red)

    # create a rectangular object for the text and surface object
    game_over_rect = game_over_surface.get_rect()
    # setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)
     
    # blit wil draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
     
    # after 5 seconds we will quit the program
    time.sleep(5)
    # deactivating pygame library
    pygame.quit()
     
    # quit the program
    quit()


# Main Function
while True:
    foodNumber=10
    speed=7
    
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_SPACE:
                pause()
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

 
    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 5
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 5
        
        #snake_body.append(fruit)
        if score>int(hiscore):
            hiscore=score
        fruit_spawn = False
    else:
        snake_body.pop()
         
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
    
    

    for pos in snake_body:
        #changing colour of food and snake 
        if(score%2==0):
            pygame.draw.rect(game_window,a,pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(game_window,b, pygame.Rect(fruit_position[0], fruit_position[1], 10,10))
        else:
            pygame.draw.rect(game_window, c ,pygame.Rect(pos[0], pos[1], 10, 10))
            pygame.draw.rect(game_window, d , pygame.Rect(fruit_position[0], fruit_position[1], 10,10,))
        
    snake_x = snake_x + snake_speed
    snake_y = snake_y + snake_speed

    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list)>snk_length:
        del snk_list[0]
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    # displaying score countinuously
    show_score(1, white, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refres Rate
    fps.tick(snake_speed)
