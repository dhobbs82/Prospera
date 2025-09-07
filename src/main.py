"""
Main entry point for the Snake Game.
Handles game initialization, event loop, and collision detection.

Group Prospera
Authors: 

Brunner, John
Carrol, Josh
Hobbs, Derrick
Montgomery, Samuel
Reece, Manu
"""

from turtle import Screen
import time

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from logger import logger

# Setup screen
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Input listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start game
logger.info("Game started.")
game_running = True

while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.head.distance(food.position()) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        logger.info("Snake ate food at position %s. Score: %d",
                    snake.head.position(), scoreboard.score)

    # Collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_running = False
            scoreboard.game_over()
            logger.warning("Snake collided with itself at %s. Final score: %d",
                           snake.head.position(), scoreboard.score)

    # Collision with wall
    if (abs(snake.head.xcor()) > (SCREEN_WIDTH / 2 - 10) or
        abs(snake.head.ycor()) > (SCREEN_HEIGHT / 2 - 10)):
        game_running = False
        scoreboard.game_over()
        logger.warning("Snake hit the wall at %s. Final score: %d",
                       snake.head.position(), scoreboard.score)

screen.exitonclick()
logger.info("Game exited by user.")
