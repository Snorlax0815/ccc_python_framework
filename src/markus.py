from datetime import datetime

from simon import Simon


class CCC():
    def lvl1_parser(self, file):
        #print(file.readlines())
        rect_points= file.readline().strip().split(",")
        #print(rect_points)
        rect_points = [float(x) for x in rect_points]
        #print(rect_points)
        num_point = int(file.readline().strip())
        #print(num_point)
        points = [file.readline().split(",") for _ in range(num_point)]
        points = [[float(x), float(y)] for x, y in points]
        #print(points)
        print(rect_points, points)
        return [rect_points, points]

    def lvl1_executor(self, data):
        rect_points = data[0]
        points = data[1]
        s = Simon()
        s.readRect(rect_points[0], rect_points[1], rect_points[2], rect_points[3])
        for point in points:
            s.addPoint(point[1], point[0])
        print(s.pointsInsideRect)
        return s.pointsInsideRect

    def lvl2_parser(self, file):
        num_cars = int(file.readline().strip())
        cars = [line.strip().split(",") for line in file.readlines()]
        cars = [[x, y, float(v), float(h)] for x, y, v, h in cars]
        print(num_cars, cars)
        return [num_cars, cars]

    def lvl2_executor(self, data):
        s = Simon()
        cars = data[1]
        for car in cars:
            s.addCar(car)
        # return f"{s.northestCar}, {s.eastestCar}"
        return f"{s.northestCar[0]},{s.northestCar[1]},{s.eastestCar[0]},{s.eastestCar[1]}"

    def lvl3_parser(self, file):
        rect_points = file.readline().strip().split(",")
        rect_points = [float(x) for x in rect_points]
        num_cars = int(file.readline().strip())
        cars = [line.strip().split(",") for line in file.readlines()]
        cars = [[x, y, float(v), float(h)] for x, y, v, h in cars]
        return [rect_points, num_cars, cars]

    def lvl3_executor(self, data):
        s = Simon()
        s.readRect(data[0][0], data[0][1], data[0][2], data[0][3])
        cars = data[2]
        for car in cars:
            s.addCarInRect(car)

        sorted = [car[0] for car in s.carsInsideRect]
        sorted.sort()
        sorted = [x for x in set(sorted)]
        sorted.sort()

        return ",".join(sorted)

    def lvl4_parser(self, file):
        num_points = int(file.readline().strip())
        lines = []
        for i in range(num_points):
            temp = file.readline().strip().split(',')
            lines.append(temp)
            
        # points = [line.strip().split(",") for line in file.readlines()]
        points = [[float(x), float(y)] for x, y in lines]
        num_edges = int(file.readline().strip())
        edges = [line.strip().split(",") for line in file.readlines()]
        edges = [[float(x), float(y)] for x, y in edges]
        return [num_points, points, num_edges, edges]

    def lvl4_executor(self, data):
        s = Simon()
        points = data[1]
        edges = data[3]
        s.readPolygon(points)

        for points in edges:
            s.addPointPolygon(points)

        print(s.pointsInsidePolygon)
        return (s.pointsInsidePolygon)

    def lvl5_parser(self, file):
        num_points_poly1 = int(file.readline().strip())
        lines =[]
        for i in range(num_points_poly1):
            temp = file.readline().strip().split(',')
            lines.append(temp)
        points_poly1 = [[float(x), float(y)] for x, y in lines]
        num_points_poly2 = int(file.readline().strip())
        lines =[]
        for i in range(num_points_poly2):
            temp = file.readline().strip().split(',')
            lines.append(temp)
        points_poly2 = [[float(x), float(y)] for x, y in lines]
        num_cars = int(file.readline().strip())
        cars = [line.strip().split(",") for line in file.readlines()]
        cars = [[x, datetime.strptime(y, "%H:%M:%S").time(), float(v), float(h)] for x, y, v, h in cars]
        return [num_points_poly1, points_poly1, num_points_poly2, points_poly2, num_cars, cars]

    def lvl5_executor(self, data):
        s = Simon()
        poly1 = data[1]
        poly2 = data[3]
        cars = data[5]
        s.readPolygon(poly1)
        s.readSecondPolygon(poly2)
        for car in cars:
            s.addObservation(car)


if __name__ == '__main__':
    ccc = CCC()
    lvl5_parser = ccc.lvl5_parser
    lvl5_executor = ccc.lvl5_executor
    data = lvl5_parser(open("../source_files/level4/level4-1.in", "r"))
    print(lvl5_executor(data))
    """lvl1_executor = ccc.lvl1_executor
    data = lvl1_parser(open("../source_files/level1/level1-1.in", "r"))
    lvl1_executor(data)"""
