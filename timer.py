import pygame as pg
from constants import *


class XmasTimer:
    def __init__(self):
        self.font = pg.font.Font("Playful.otf", 112)
        self.text = None
        self.shadow = None

    def get_time(self, days, time_left):
        formatted_string = f"({days}:{time_left})"

        self.text = self.font.render(formatted_string, True, (255, 25, 25))
        self.shadow = self.font.render(formatted_string, True, "black")

    def draw(self, screen: pg.Surface):
        screen.blit(self.shadow, ((WIN_WIDTH / 2) - (self.text.get_width() / 2) - 5,
                                  (WIN_HEIGHT / 2 - (self.text.get_height() / 2)) - 5))

        screen.blit(self.text, ((WIN_WIDTH / 2) - (self.text.get_width() / 2),
                                (WIN_HEIGHT / 2 - (self.text.get_height() / 2))))
