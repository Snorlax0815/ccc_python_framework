from src.simon import Simon


class CCC():
    def lvl1_parser(self, file):
        num_rectangles = (file.readline())
        print(num_rectangles)
        rect_points= file.readline.split(",")
        print(rect_points)
        num_point = int(file.readline().strip())
        print(num_point)
        points = [file.readline().split(",") for _ in range(num_point)]
        points = [(int(x), int(y)) for x, y in points]
        print(points)
        return rect_points, points

    def lvl1_executor(self, rect_points, points):
        s = Simon()
        s.readRect(rect_points[0], rect_points[1], rect_points[2], rect_points[3])
        for point in points:
            s.addPoint(point[1], point[0])
        print(s.pointsInsideRect)
        pass



if __name__ == '__main__':
    ccc = CCC()

    lvl1_parser = ccc.lvl1_parser
    lvl1_executor = ccc.lvl1_executor
    rect_points, points = lvl1_parser(open("../source_files/level1/level1.in", "r"))
    lvl1_executor(rect_points, points)
