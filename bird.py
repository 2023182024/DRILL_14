import random

from pico2d import get_canvas_width, load_image

import game_framework


class Bird:
    FRAME_WIDTH = 180
    FRAME_HEIGHT = 150
    DRAW_WIDTH = 100
    DRAW_HEIGHT = 83
    FRAME_COUNT = 14
    FRAME_PER_SECOND = 10
    SPEED = 180

    def __init__(self):
        self.x = random.randint(
            self.DRAW_WIDTH // 2,
            get_canvas_width() - self.DRAW_WIDTH // 2,
        )
        self.y = 400
        self.frame = 0
        self.direction = 1
        self.image = load_image('bird_animation.png')

    def update(self):
        self.x += self.direction * self.SPEED * game_framework.frame_time

        left = self.DRAW_WIDTH // 2
        right = get_canvas_width() - left
        if self.x >= right:
            self.x = right
            self.direction = -1
        elif self.x <= left:
            self.x = left
            self.direction = 1

        self.frame = (self.frame + self.FRAME_PER_SECOND *
                      game_framework.frame_time) % self.FRAME_COUNT

    def draw(self):
        frame = int(self.frame)
        column = frame % 5
        row = 2 - frame // 5
        flip = '' if self.direction == 1 else 'h'
        self.image.clip_composite_draw(
            column * self.FRAME_WIDTH,
            row * self.FRAME_HEIGHT,
            self.FRAME_WIDTH,
            self.FRAME_HEIGHT,
            0,
            flip,
            self.x,
            self.y,
            self.DRAW_WIDTH,
            self.DRAW_HEIGHT,
        )
