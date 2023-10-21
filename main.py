import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
player = Player()
Cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    Cars.create_cars()
    Cars.move_cars()
    for car in Cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()
    if player.finished():
        player.reset_pos()
        Cars.level_up()
        score.level_up()

screen.exitonclick()

