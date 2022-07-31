import pygame


class Tilesheet:
    """sub division on a image file"""
    def __init__(self, filename, width, height, map_width, map_height):
        image = pygame.image.load(filename)

        self.tile_table = []
        self.rows = map_height // height  # number of rows equiv to partion of column space
        self.cols = map_width // width

        for tile_x in range(0, self.cols):
            line = []
            self.tile_table.append(line)
            for tile_y in range(0, self.rows):
                rect = (tile_x * width, tile_y * height, width, height)
                line.append(image.subsurface(rect))

    def draw(self, screen, spacingx=72, spacingy=72):
        """blit the entire tile set with sub division spacing"""
        for x, row in enumerate(self.tile_table):
            for y, tile in enumerate(row):
                screen.blit(tile, (x * spacingx, y * spacingy))

    def get_tile(self, x, y=None):
        """get a tile from the tile_table at position x, y optionally choose tile with array if y is not given"""
        if y:
            return self.tile_table[x][y]
        else:
            return self.tile_table[x[0]][x[1]]
