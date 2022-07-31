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

    def convex_hull_graham(points):
        '''
        Returns points on convex hull in CCW order according to Graham's scan algorithm.
        By Tom Switzer <thomas.switzer@gmail.com>.
        '''
        TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

        def cmp(a, b):
            return (a > b) - (a < b)

        def turn(p, q, r):
            return cmp(
                (q[0] - p[0]) * (r[1] - p[1]) - (r[0] - p[0]) * (q[1] - p[1]),
                0)

        def _keep_left(hull, r):
            while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
                hull.pop()
            if not len(hull) or hull[-1] != r:
                hull.append(r)
            return hull

            points = sorted(points)
            l = reduce(_keep_left, points, [])
            u = reduce(_keep_left, reversed(points), [])
            return l.extend(u[i] for i in range(1, len(u) - 1)) or l

    def twodimensionalsum(self, p1 , p2):
        """given (a,b) and (c,d) return (a+c, b+d)"""
        return (p1[0] + p2[0], p1[1] + p2[1])