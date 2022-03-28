
import time 
from turtle import Screen 
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

timmy = Player()


screen.listen()
screen.onkey(timmy.go_up, "Up")
screen.onkey(timmy.go_down, "Down")

game_is_on = True
while game_is_on:
       time.sleep(0.1)
       screen.update()

