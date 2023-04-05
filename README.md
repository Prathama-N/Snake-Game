# Snake-Game

In the game of Snake, the player uses the arrow keys to move a "snake" around 
the board. There is even a background music added to this game. As the snake 
finds food, it eats the food, and thereby grows larger. The game ends when the 
snake either moves off the screen or moves into itself. The goal is to make the 
snake as large as possible before that happens. The player is represented as 
snake, which grows if it eats an apple. The goal of the game is to eat as many 
apples as possible without colliding into you. This is very easy in the early phase 
of the game but is increasingly more difficult as the length of the snake grows. 
The snake game has some rules: 
1. If the snake eats an apple, the apple moves to a new position.

2. once the snake eats the apple, the color of snake and fruit will be changed 
according to the players choice.
2. If the snake eats an apple, the snake’s length grows.
3. If a snake collapses with itself or hits the wall, game over.
4. High score will be displayed if the player has got high score or else score will 
be displayed.
5. If the player wants to quit the game anytime,they can use esc key. 
6.If the player wants to pause and resume the game anytime, they can use 
SPACE bar.
A player object can be created and variables can be modified using the 
movement methods. We link those methods to the events. 
 
In the PYGAME module we can import/define functions which would help us in 
creating the game in an interactive manner.

# ALGORTIHM
Step-1: START<br>
Step-2: Importing modules<br>
Step-3: Printing instructions for playing game<br>
Step-4: Input name, snake_colour1, food_colour1, snake_colour2,food_colour2<br>
Step-5: Creating a window<br>
Step-6: Setting a Background color and music<br>
Step-7: Initializing the game<br>
Step-8: Snake starts moving:<br>
 if(key==up) then moves UP<br>
 if(key==down) then moves DOWN<br>
 if(key ==right) then moves RIGHT<br>
  if(key==left) then moves LEFT<br>
Step-9: If snake meets the food, node is incremented and new food is
generated.<br>
Step-10: If(score==odd) then change snake to snake_colour1 and food to food_colour1
<br> else change snake to snake_colour2 and food to food_colour2<br>
Step-11: if(key==space) then snake stops moving.<br>
 else it continues the process<br>
Step-12: if(key==esc) then EXIT the game<br>
 else it continues the process<br>
Step-13: if(score>=hiscore) then Print hiscore<br>
 else print score<br>
Step-14: END<br>
