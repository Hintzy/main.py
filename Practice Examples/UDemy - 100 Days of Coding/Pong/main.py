from turtle import Screen
from paddle import Paddle
from time import sleep
from game import PongGame


# screen initializations
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

# object initializations
p1 = Paddle('P1')
p2 = Paddle('P2')
game = PongGame()

# set controls
screen.onkeypress(p1.up(), 'w')
screen.onkeypress(p1.down(), 's')
screen.onkeypress(p2.up(), 'Up')
screen.onkeypress(p2.down(), 'Down')

while game.game_on:
    screen.update()

    # print(p1.player)
    # print(p1.start_squares)
    # print(p1.segs)
    # print(p2.player)
    # print(p2.start_squares)
    # print(p2.segs)
    sleep(0.5)

screen.exitonclick()





