import pygame
from game.constants import *


class Brush:
    def __init__(self, inherit_screen, inherit_layers, inherit_tiles,
                 inherit_grid):
        """brush tooling"""
        self.desc = "brush tools!"
        self.grid = inherit_grid
        self.tiles = inherit_tiles
        self.screen = inherit_screen
        self.layers = inherit_layers
        self.tile_controller = TILE_CONTROLLER
        self.maxflag = False

    def draw_border(self, x, y, overlap="next"):
        # self.draw_tile_at(x, y)
        # x,y are GRID CORDINATES NEAREST TO MOUSE when shift is pressed
        tilex = self.grid.rounder(x)
        tiley = self.grid.rounder(y)
        screenx = self.grid.round_num(x)
        screeny = self.grid.round_num(y)
        line_color = (255, 0, 0)
        line_highlight = (0, 255, 0)
        points = [[(0, 24), (15, 31), (15, 16), (0, 7)],
                  [(31, 24), (16, 31), (16, 16), (31, 7)],
                  [(1, 7), (15, 15), (31, 7), (15, 0)]]
        relpoints = []
        for point in points:
            relpoints.append([(point[0][0] + x, point[0][1] + y),
                              (point[1][0] + x, point[1][1] + y),
                              (point[2][0] + x, point[2][1] + y),
                              (point[3][0] + x, point[3][1] + y)])

        # left = pygame.draw.polygon(self.screen, line_color, relpoints[0])
        # right= pygame.draw.polygon(self.screen, line_color, relpoints[1])
        # top  = pygame.draw.polygon(self.screen, line_color, relpoints[2])

        colliderleft = self.grid.poly_check(relpoints[0],
                                            pygame.mouse.get_pos())
        colliderright = self.grid.poly_check(relpoints[1],
                                             pygame.mouse.get_pos())
        collidertop = self.grid.poly_check(relpoints[2],
                                           pygame.mouse.get_pos())

        # when placing a tile at face of a tile side tiles will be added to
        # same layer. this half layer is also the top of the lower layer

        if collidertop == True:
            # pygame.draw.polygon(self.screen, line_highlight, relpoints[2])
            # pygame.draw.polygon(self.screen, line_color, relpoints[0])
            # pygame.draw.polygon(self.screen, line_color, relpoints[1])
            self.draw_adjecent_face(overlap=overlap, face="top", x=x, y=y)

        elif colliderleft == True:
            # pygame.draw.polygon(self.screen, line_highlight, relpoints[0])
            # pygame.draw.polygon(self.screen, line_color, relpoints[1])
            # pygame.draw.polygon(self.screen, line_color, relpoints[2])
            self.draw_adjecent_face(overlap=overlap, face="left", x=x, y=y)

            print("collided with left", tilex, tiley)
            self.layers[tiley][tilex][tiley][1] = tilex - .5, tiley

        elif colliderright == True:
            # pygame.draw.polygon(self.screen, line_highlight, relpoints[1])
            # pygame.draw.polygon(self.screen, line_color, relpoints[0])
            # pygame.draw.polygon(self.screen, line_color, relpoints[2])
            self.draw_adjecent_face(overlap=overlap, face="right", x=x, y=y)
            print("collided with right", tilex, tiley)
            self.layers[tiley][tilex][tiley][2] = tilex + .5, tiley

        # print("collider", collider)
        # print("collideleft", collideleft)

    def draw_tile_at(self, x, y):
        """doubles as setter for y as z will choose a integer division from
        y // 32 as a layer """
        # round to nearest base layer
        # place adjacent horizontal edged tiles

        tilex = self.grid.rounder(x)
        tiley = self.grid.rounder(y)
        screenx = self.grid.round_num(x)
        screeny = self.grid.round_num(y)
        self.layers[tiley][tilex][
            tiley][0] = tilex, tiley
        self.screen.blit(self.tiles.get_tile(self.tile_controller),
                         (screenx, screeny))

    def draw_adjecent_at(self, x, y):
        terrainbase = self.tiles.get_tile(self.tile_controller)
        self.screen.blit(terrainbase, (x, y))

    def draw_adjecent_face(self,
                           visible=True,
                           overlap="next",
                           face="top",
                           x=0,
                           y=0):
        """from origin, draw adjecent faces
        visible: indicates if the face is visible, if false place tile normal to
        face
        overlap: indicates if new tile should be "prev" or "next" being top
        layer to view
        face: indicates which face to draw "top", "left", "right"
        x, y: indicates where to draw the face in relation to.
        """
        # self.screen.fill(self.bg_color)
        terrainbase = self.tiles.get_tile(self.tile_controller)

        half_shift = TILESIZE // 2
        quarter_shift = TILESIZE // 4
        shift_visible = \
        [(0,-half_shift), (-half_shift, quarter_shift), (half_shift,
                                                          quarter_shift)]

        # shift array for placing adjacent tiles
        # order top, left, right invisible bottom , normal right, normal left

        if visible and face == "top":
            if overlap == "next":
                self.screen.blit(terrainbase, (x, y))
                self.screen.blit(
                    terrainbase,
                    self.grid.twodimensionalsum((x, y), shift_visible[0]))
            elif overlap == "prev":
                self.screen.blit(
                    terrainbase,
                    self.grid.twodimensionalsum((x, y), shift_visible[0]))
                self.screen.blit(terrainbase, (x, y))
            elif overlap == "curr":
                self.screen.blit(
                    terrainbase,
                    self.grid.twodimensionalsum((x, y), shift_visible[0]))

        elif visible and face == "left":
            if overlap == "next":
                self.screen.blit(terrainbase, (x, y))
                self.screen.blit(
                    terrainbase,
                    self.grid.twodimensionalsum((x, y), shift_visible[1]))
            elif overlap == "prev":
                self.screen.blit(
                    terrainbase,
                    self.grid.twodimensionalsum((x, y), shift_visible[1]))
                self.screen.blit(terrainbase, (x, y))
            elif overlap == "curr":
                self.screen.blit(
                    terrainbase,
                    self.grid.twodimensionalsum((x, y), shift_visible[1]))
        elif visible and face == "right":
            if overlap == "next":
                self.screen.blit(terrainbase, (x, y))
                self.screen.blit(
                    terrainbase,
                    self.grid.twodimensionalsum((x, y), shift_visible[2]))
            elif overlap == "prev":
                self.screen.blit(
                    terrainbase,
                    self.grid.twodimensionalsum((x, y), shift_visible[2]))
                self.screen.blit(terrainbase, (x, y))
            elif overlap == "curr":
                self.screen.blit(
                    terrainbase,
                    self.grid.twodimensionalsum((x, y), shift_visible[2]))


class UI():

    def __init__(self, inheritbrush):
        self.font = pygame.font.Font(FONT_PATH, FONT_SIZE)
        self.brush_layer1 = BRUSH_INIT_1
        self.brush_layer2 = BRUSH_INIT_2

        self.screen = inheritbrush.screen
        self.layers = inheritbrush.layers
        self.tiles = inheritbrush.tiles

        self.brush = inheritbrush  # use for tile_controller and math with grid

    def draw_brush_toggle(self, toggle):
        """draw the current brush toggle:1 [curr, next, prev], toggle:2 [place, delete] """
        if toggle == 0:
            if self.brush_layer1 == "curr":
                return setattr(self, "brush_layer1", "next")
            if self.brush_layer1 == "next":
                return setattr(self, "brush_layer1", "prev")
            if self.brush_layer1 == "prev":
                return setattr(self, "brush_layer1", "curr")

        if toggle == 1:
            if self.brush_layer2 == "place":
                return setattr(self, "brush_layer2", "delete")
            if self.brush_layer2 == "delete":
                return setattr(self, "brush_layer2", "place")

        if toggle == 2:

            if self.brush.maxflag:
                # print("Reseting after max has been reached")
                self.brush.tile_controller = tuple((0, 0))
                self.brush.maxflag = False
            else:
                if ((self.brush.tile_controller[0] + 1) %
                    (self.tiles.cols) != 0):
                    self.brush.tile_controller = (
                        self.brush.tile_controller[0] + 1,
                        self.brush.tile_controller[1])
                else:
                    self.brush.tile_controller = (
                        0, self.brush.tile_controller[1] + 1)

            if 0 <= (
                (self.brush.tile_controller[0] + 1) *
                (self.brush.tile_controller[1] + 1)
            ) < self.tiles.rows * self.tiles.cols and not self.brush.maxflag:
                print(self.brush.tile_controller[0] + 1,
                      self.brush.tile_controller[1] + 1, self.tiles.cols,
                      self.tiles.rows)

                # traverse one full row from (0, 0) then go to next column left most
            else:
                # print("max reached", self.brush.tile_controller[0] + 1,
                #       self.brush.tile_controller[1] + 1)
                # self.brush.tile_controller = ()
                self.brush.maxflag = True

    def draw_brush_display(self):
        """draw the current brush toggle position for index 0 (overlap) and 1 (deletion)"""
        render_brush = self.font.render(
            " Brush Overlap: " + str(self.brush_layer1) +
            " | Brush Placement: " + str(self.brush_layer2) +
            " | Tilesheet Block: " + str(self.brush.tile_controller[0] + 1) +
            "x" + str(self.brush.tile_controller[1] + 1), True, WHITE)
        font_height = SCREEN_HEIGHT - FONT_SIZE
        pygame.draw.rect(
            self.screen, BLACK,
            pygame.Rect(0, self.brush.grid.round_num(font_height),
                        SCREEN_WIDTH, SCREEN_HEIGHT))

        self.screen.blit(render_brush, (0, SCREEN_HEIGHT - FONT_SIZE))

    def detected_tile(self, posx, posy, overlap="next", deletion=BRUSH_INIT_2):
        tilex = self.brush.grid.rounder(posx)
        tiley = self.brush.grid.rounder(posy)
        screenx = self.brush.grid.round_num(posx)
        screeny = self.brush.grid.round_num(posy)
        # print(self.brush.grid.is_nan(tilex, tiley))
        if not self.brush.grid.is_nan(tilex, tiley):
            if deletion == BRUSH_INIT_2:
                self.brush.draw_border(screenx,screeny, overlap)


            return True
        else:
            return False
