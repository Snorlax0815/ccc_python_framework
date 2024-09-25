class CCC():
    def lvl1_parser(self, file):
        num_lines = file.readline()
        return [file.readline() for _ in range(int(num_lines))]

    def lvl1_executor(self, data):
        out = []
        for line in data:
            output_line = str(line.count("W")) + " " + str(line.count("D")) + " " + str(line.count("S")) + " " + str(line.count("A"))
            print(output_line)
            out.append(output_line)
        print(out)
        return "\n".join(out)


if __name__ == '__main__':
    ccc = CCC()

    lvl1_parser = ccc.lvl1_parser
    lvl1_executor = ccc.lvl1_executor
    data = lvl1_parser(open("source_files/level1/level1_example.in", "r"))
    lvl1_executor(data)
