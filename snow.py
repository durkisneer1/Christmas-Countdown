import pygame as pg
from math import sin, radians
from random import randint
from constants import *


class Snowflake(pg.sprite.Sprite):
    def __init__(self, groups: pg.sprite.Group):
        super().__init__(groups)

        self.surf = pg.Surface((10, 10)).convert()
        self.surf.fill("white")

        self.direction = randint(0, 1)
        self.x_offset = randint(0, WIN_WIDTH)
        self.pos = pg.Vector2(self.x_offset, -self.surf.get_height())

        self.angle = 0
        self.vel = randint(9, 15)
        self.sway = self.vel * 2

    def fall(self, dt):
        self.pos.y += self.vel * dt
        self.pos.x = (sin(radians(self.angle)) * self.sway) + self.x_offset

        if self.direction == 1:
            self.angle += self.sway * dt
        else:
            self.angle -= self.sway * dt

        if self.pos.y > WIN_HEIGHT:
            self.kill()

    def draw(self, screen: pg.Surface):
        screen.blit(self.surf, self.pos)
