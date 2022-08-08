import numpy as np
from game.constants import *


class Grid:
    INT_MAX = 10000

    def __init__(self):

        self.desc = "This object is used to do math with vectors."

        gridwidth = SCREEN_WIDTH // TILESIZE
        gridheight = SCREEN_HEIGHT // TILESIZE

        #layer v2 [y overlap][x screen][y screen]
        self.layers = np.empty((gridheight, gridwidth, gridheight,
                                2, 2),
                               np.float32)
        self.layers[:] = np.nan

    def poly_check(self, points, p):

        ax, ay, bx, by, cx, cy, dx, dy = points[0][0], points[0][1], \
                                         points[1][0], points[1][1], \
                                         points[2][0], points[2][1], \
                                         points[3][0], points[3][1]
        px, py = p[0], p[1]
        nx = bx - ax
        ny = by - ay
        edge = (px - ax) * ny + (py - ay) * (-nx)
        if (edge > 240):
            return False
        else:
            nx = cx - bx
            ny = cy - by
            edge = (px - bx) * ny + (py - by) * (-nx)

        if (edge > 240):
            return False
        else:
            nx = dx - cx
            ny = dy - cy
            edge = (px - cx) * ny + (py - cy) * (-nx)

        if (edge > 240):
            return False
        else:
            nx = ax - dx
            ny = ay - dy
            edge = (px - dx) * ny + (py - dy) * (-nx)

        if (edge > 240):
            return False
        else:
            return True

    def twodimensionalsum(self, p1, p2):
        """given (a,b) and (c,d) return (a+c, b+d)"""
        return (p1[0] + p2[0], p1[1] + p2[1])

    def round_num(self, number, roundby=None):
        """if roundby is none default to TILESIZE constant"""
        if not roundby:
            return TILESIZE * (number // TILESIZE)
        else:
            return roundby * (number // roundby)

    def rounder(self, number, roundby=None):
        """same as round_num but no scalar if rounder is none default to TILESIZE constant"""
        if not roundby:
            return (number // TILESIZE)
        else:
            return (number // roundby)

    def is_nan(self, tilex, tiley):
        """check if self.layers has any nan values at bone layer"""
        if np.isnan(self.layers[tiley][tilex][tiley][0][0]):
            return True
        else:
            return False