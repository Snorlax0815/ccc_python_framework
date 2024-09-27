class Simon:
    def __init__(self) -> None:
        self.pointsInsideRect = 0
        self.points = []

        self.northestCar = ['uwu', None, 0, 0]
        self.eastestCar = ['uwu', None, 0, 0]

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

    def addCar(self, data):
        if(data[2] > self.northestCar[2]):
            self.northestCar = data

        if data[3] > self.eastestCar[3]:
            self.eastestCar = data
