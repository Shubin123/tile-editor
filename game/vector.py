import numpy as np
class Grid:
    INT_MAX = 10000

    def __init__(self):

        self.desc = "This object is used to do math with vectors."


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


    def twodimensionalsum(self, p1 , p2):
        """given (a,b) and (c,d) return (a+c, b+d)"""
        return (p1[0] + p2[0], p1[1] + p2[1])