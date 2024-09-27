class Simon:
    def __init__(self) -> None:
        self.pointsInsideRect = 0
        self.points = []

    # read a rectangle via north, east, south and west coords
    def readRect(self, n, o, s, w):
        self.n = n
        self.o = o
        self.s = s
        self.w = w

    # add a point (x and y coords) 
    def addPoint(self, x, y):
        pass
        # self.points.append((l, m))
        # if self.w < l and l < self.o and m 
