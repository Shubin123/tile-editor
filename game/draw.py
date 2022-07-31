import pygame
from game.vector import Grid
from game.constants import *


class Brush:
    def __init__(self, inherit_screen, inherit_layers, inherit_tiles):
        """brush tooling"""
        self.desc = "brush tools!"
        self.grid = Grid()

        self.tiles = inherit_tiles
        self.screen = inherit_screen
        self.layers = inherit_layers

    def draw_border(self, x, y, overlap="next"):
        # self.draw_tile_at(x, y)
        # x,y are GRID CORDINATES NEAREST TO MOUSE when shift is pressed
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
            half_y = (y // (TILESIZE))
            half_x = (x // (TILESIZE)) - .5
            print("collided with left", half_x, half_y)
            self.layers[y // TILESIZE].add((half_x, half_y))

        elif colliderright == True:
            # pygame.draw.polygon(self.screen, line_highlight, relpoints[1])
            # pygame.draw.polygon(self.screen, line_color, relpoints[0])
            # pygame.draw.polygon(self.screen, line_color, relpoints[2])
            self.draw_adjecent_face(overlap=overlap, face="right", x=x, y=y)
            half_y = (y // (TILESIZE))
            half_x = (x // (TILESIZE)) + .5
            print("collided with right", half_x, half_y)
            self.layers[y // TILESIZE].add((half_x, half_y))

        # print("collider", collider)
        # print("collideleft", collideleft)

    def draw_terrain(self):
        self.screen.fill(self.bg_color)
        terrainbase = self.tiles.get_tile(0, 0)
        block_size = 32
        # self.screen.blit(terrainbase, (32, 0))
        # self.screen.blit(terrainbase, (16, 8))
        self.screen.blit(terrainbase, (0, 0))
        # left edge
        # self.screen.blit(terrainbase, (16, 8))
        self.screen.blit(terrainbase, (32, 16))

    def draw_tile_at(self, x, y):
        """doubles as setter for y as z will choose a integer division from
        y // 32 as a layer """
        layer_height = TILESIZE * (y // TILESIZE
                                   )  # round to nearest base layer
        edge_place = TILESIZE * (x // TILESIZE
                                 )  # place adjacent horizontal edged tiles
        self.layers[y // TILESIZE].add((x // TILESIZE, y // TILESIZE))
        print("layer map at draw tile call", self.layers)
        self.screen.blit(self.tiles.get_tile(0, 0), (edge_place, layer_height))

    def draw_adjecent_at(self, x, y):
        baseterrain = self.tiles.get_tile(0, 0)
        self.screen.blit(baseterrain, (x, y))

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
        terrainbase = self.tiles.get_tile(0, 0)

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
        self.brush_layer = BRUSH_INIT
        self.screen = inheritbrush.screen
        self.layers = inheritbrush.layers
        self.brush = inheritbrush

    def draw_brush_toggle(self):
        """draw the current brush toggle [curr, next, prev] """
        # self.font.render("Brush: " + str(self.brush_layer), True, WHITE)
        if self.brush_layer == "curr":
            return setattr(self, "brush_layer", "next")
        if self.brush_layer == "next":
            return setattr(self, "brush_layer", "prev")
        if self.brush_layer == "prev":
            return setattr(self, "brush_layer", "curr")

    def draw_brush_display(self):
        """draw the current brush toggle [curr, next, prev] """
        render_brush = self.font.render("Brush: " + str(self.brush_layer),
                                        True, WHITE)
        pygame.draw.rect(
            self.screen, BLACK,
            pygame.Rect(0, SCREEN_HEIGHT - 32, SCREEN_WIDTH, SCREEN_WIDTH))
        self.screen.blit(render_brush, (0, SCREEN_HEIGHT - FONT_SIZE))

    def detected_tile(self, pos, overlap="next"):
        """detected tile is meant for base tiles"""
        for layer in self.layers:
            for tile in layer:
                if tile[0] == (pos[0]//TILESIZE) and tile[1] == \
                        (pos[1]//TILESIZE):

                    self.brush.draw_border(tile[0] * TILESIZE,
                                           tile[1] * TILESIZE, overlap)

                    return True, pos
        return False
