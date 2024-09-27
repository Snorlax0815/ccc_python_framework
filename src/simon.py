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
        self.points.append((x, y))
        if self.w < x and x < self.o and self.n > y and y > self.s:
            self.pointsInsideRect += 1
