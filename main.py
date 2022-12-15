import pygame as pg
import time
from datetime import datetime
from constants import *
from timer import XmasTimer
from snow import Snowflake

pg.init()
screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pg.display.set_caption("Christmas Countdown")
clock = pg.time.Clock()

wallpaper = pg.image.load("wallpaper.png").convert()
wallpaper = pg.transform.scale(wallpaper, (WIN_WIDTH, WIN_HEIGHT))

snow_group = pg.sprite.Group()
spawn_snow = pg.USEREVENT + 1
pg.time.set_timer(spawn_snow, 250)

xmas_time = datetime(year=2022, month=12, day=25)
show_timer = XmasTimer()


def main():
    run = True
    while run:
        dt = clock.tick() / 100
        for ev in pg.event.get():
            if ev.type == pg.QUIT or (ev.type == pg.KEYDOWN and ev.key == pg.K_ESCAPE):
                run = False

            if ev.type == spawn_snow:
                Snowflake(snow_group)

        current_time = datetime.now()
        time_left = xmas_time - current_time
        show_timer.get_time(time_left.days, time.strftime("%H:%M:%S", time.gmtime(time_left.seconds)))

        screen.blit(wallpaper, (0, 0))
        for snow in snow_group:
            snow.fall(dt)
            snow.draw(screen)
        show_timer.draw(screen)

        pg.display.flip()


if __name__ == '__main__':
    main()
