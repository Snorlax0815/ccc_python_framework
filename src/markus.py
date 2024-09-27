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
        return f"{s.northestCar}, {s.eastestCar}"


if __name__ == '__main__':
    ccc = CCC()
    lvl2_parser = ccc.lvl2_parser
    lvl2_executor = ccc.lvl2_executor
    data = lvl2_parser(open("../source_files/level2/level2-1.in", "r"))
    print(lvl2_executor(data))
    """lvl1_executor = ccc.lvl1_executor
    data = lvl1_parser(open("../source_files/level1/level1-1.in", "r"))
    lvl1_executor(data)"""
