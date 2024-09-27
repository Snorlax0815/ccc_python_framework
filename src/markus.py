class CCC():
    def lvl1_parser(self, file):
        num_rectangles = (file.readline())
        print(num_rectangles)
        rect_points= file.readline.split(",")
        print(rect_points)
        num_point = int(file.readline().strip())
        print(num_point)
        points = [file.readline().split(",") for _ in range(num_point)]
        print(points)
        return rect_points, points

    def lvl1_executor(self, data):
        # simon object erstellen,
        # rectangle erstellen
        # punkte übergeben
        pass



if __name__ == '__main__':
    ccc = CCC()

    lvl1_parser = ccc.lvl1_parser
    lvl1_executor = ccc.lvl1_executor
    data = lvl1_parser(open("source_files/level1/level1_example.in", "r"))
    lvl1_executor(data)
