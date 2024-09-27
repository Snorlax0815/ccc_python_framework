class Simon:
    def __init__(self) -> None:
        self.pointsInsideRect = 0
        self.points = []

        self.northestCar = ['uwu', None, 0, 0]
        self.eastestCar = ['uwu', None, 0, 0]

        self.carsInsideRect = []

        self.pointsInsidePolygon = 0

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

    def checkInsideRect(self, x, y):
        return  self.w < x and x < self.o and self.n > y and y > self.s

    def addCar(self, data):
        if(data[2] > self.northestCar[2]):
            self.northestCar = data

        if data[3] > self.eastestCar[3]:
            self.eastestCar = data

    def addCarInRect(self, data):
        if self.checkInsideRect(data[3], data[2]):
            self.carsInsideRect.append(data)

    def readPolygon(self, data):
        self.polygon = data
        print(f"read polygon {data}")

    def is_point_in_convex_polygon(self, data):
        point = [data[1], data[0]]
        polygon = self.polygon
        """
        Determine if a point is inside a convex polygon using the ray-casting algorithm.

        :param point: A tuple (x, y) representing the point.
        :param polygon: A list of tuples [(x1, y1), (x2, y2), ...] representing the vertices of the polygon.
        :return: True if the point is inside the polygon, False otherwise.
        """
        x, y = point[1], point[0]
        n = len(polygon)
        inside = False

        p1x, p1y = polygon[0]
        for i in range(n + 1):
            p2x, p2y = polygon[i % n][0], polygon[i % n][1]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside
    
    def addPointPolygon(self, data):
        if self.is_point_in_convex_polygon(data):
            self.pointsInsidePolygon += 1

