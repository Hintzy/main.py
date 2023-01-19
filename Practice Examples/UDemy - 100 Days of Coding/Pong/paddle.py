from turtle import Turtle

START_POS = {
    'P1': [(-380, 50), (-380, 30), (-380, 10), (-380, -10), (-380, -30), (-380, -50)],
    'P2': [(380, 50), (380, 30), (380, 10), (380, -10), (380, -30), (380, -50)]
}
PADDLE_SPEED = 5


class Paddle(Turtle):
    def __init__(self, player_num):
        super().__init__()
        self.player = player_num
        self.start_squares = START_POS[player_num]
        self.segs = []
        self.draw_paddle()

    def draw_paddle(self):
        for point in self.start_squares:
            new_seg = Turtle(shape='square')
            new_seg.color('white')
            new_seg.speed(0)
            new_seg.pu()
            new_seg.goto(point)
            new_seg.setheading(90)
            self.segs.append(new_seg)

    def up(self):
        for seg in self.segs:
            seg.fd(20)

    def down(self):
        for seg in self.segs:
            seg.bk(20)
