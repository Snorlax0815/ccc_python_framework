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



if __name__ == '__main__':
    ccc = CCC()
    lvl1_parser = ccc.lvl1_parser
    lvl1_executor = ccc.lvl1_executor
    data = lvl1_parser(open("../source_files/level1/level1-1.in", "r"))
    lvl1_executor(data)
