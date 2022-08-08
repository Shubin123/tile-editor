import pygame
import pygame.locals

from game.tilesheet import Tilesheet
from game.draw import Brush, UI
from game.vector import Grid
from game.constants import *

import sys


class Game:
    def __init__(self):

        pygame.init()
        pygame.display.set_caption(CAPTION)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen_rect = self.screen.get_rect()

        self.clock = pygame.time.Clock()
        self.bg_color = pygame.Color('yellow')

        self.allow_left = False
        self.allow_right = False
        self.allow_middle = False

        self.tiles = Tilesheet(
            'lib/pictures/Terrain_Map.png',
            width=TILESIZE,  # assuming square tiles
            height=TILESIZE,  # we can import tile maps that are non square
            map_width=TILESHEET_SIZES[0][0],
            map_height=TILESHEET_SIZES[0][1])

        self.grid = Grid()
        self.brush = Brush(self.screen, self.grid.layers, self.tiles,
                           self.grid)
        self.ui = UI(self.brush)

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            # mouse events
            # 1 - left click
            # 2 - middle click
            # 3 - right click
            # 4 - scroll up
            # 5 - scroll down
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.allow_left = True
                    print("left click down")
                if event.button == 2:
                    self.allow_middle = True
                    print("middle click down")
                if event.button == 3:
                    self.allow_right = True
                    print("right click down")

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.allow_left = False
                    print("left click up")
                if event.button == 2:
                    self.allow_middle = False
                    print("middle click up")
                if event.button == 3:
                    self.allow_right = False
                    print("right click up")

            if event.type == pygame.MOUSEMOTION:

                if self.allow_left:
                    self.brush.draw_tile_at(pygame.mouse.get_pos()[0],
                                            pygame.mouse.get_pos()[1])

                if self.allow_right:
                    self.ui.detected_tile(pygame.mouse.get_pos()[0],
                                          pygame.mouse.get_pos()[1],
                                          overlap=self.ui.brush_layer1,
                                          deletion=self.ui.brush_layer2)
                if self.allow_middle:
                    print("this is the middle click in motion")
                    # self.ui.detected_tile(pygame.mouse.get_pos(),
                    #                       overlap="prev")

            # key events
            # toggle 0 = placement order
            # toggle 1 = deletetion or place
            # toggle 2 = tileset

            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_ESCAPE:
                #     sys.exit()
                if event.key == pygame.K_LSHIFT:
                    self.ui.draw_brush_toggle(0)
                    self.ui.draw_brush_display()
                if event.key == pygame.K_BACKSPACE:
                    self.ui.draw_brush_toggle(1)
                    self.ui.draw_brush_display()
                if event.key == pygame.K_TAB:
                    self.ui.draw_brush_toggle(2)

    def update(self):
        pygame.display.flip()
