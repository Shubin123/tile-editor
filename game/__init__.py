import pygame
import pygame.locals

from game.tilesheet import Tilesheet
from game.draw import Brush, UI
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

        self.tiles = Tilesheet('lib/pictures/Terrain_Map.png', 32, 32, 6, 8)
        self.layers = [set() for i in range(TILESIZE)] # [ {(x, y)} ]
        self.brush = Brush(self.screen, self.layers, self.tiles)
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
                    self.allow_middle =True
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
                    self.ui.detected_tile(pygame.mouse.get_pos(),
                                          overlap=self.ui.brush_layer)
                if self.allow_middle:
                    print("this is the middle click in motion")
                    # self.ui.detected_tile(pygame.mouse.get_pos(),
                    #                       overlap="prev")

            # key events
            if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_ESCAPE:
                #     sys.exit()
                if event.key == pygame.K_LSHIFT:
                    self.ui.draw_brush_toggle()
                    self.ui.draw_brush_display()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT:
                    print("shift up")

    def update(self):
        pygame.display.flip()

