from simon import solve1, test


class CCC():
    def lvl1_parser(self, file):
        num_lines = file.readline()
        outputs = []
        for line in file:
            line = line.strip().split(" ")
            outputs.append(line)
        print(outputs)
        return outputs

    def lvl1_executor(self, data):
        out = []
        for line in data:
            c = 0
            for i in line:
                c += int(i)
            out.append(c)
        print(out)
        s = ""
        for i in out:
            s += str(i) + "\n"
        s =s.strip()
        print(s)
        return s

    def lvl2_parser(self, file):
        num_lines = file.readline()
        outputs = []
        for line in file:
            line = line.strip().split(" ")
            outputs.append(line)
        print(outputs)
        return outputs

    def lvl2_executor(self, data):
        out = ""
        for l in data:
            result = solve1(l)
            out += str(result) + "\n"
        out.strip()
        return out.strip()

    def lvl3_parser(self, file):
        num_flights = file.readline()
        max_time = file.readline()
        outputs = []
        for line in file:
            line = line.strip().split(" ")
            outputs.append(line)
        print(outputs)
        return [max_time,outputs]



if __name__ == '__main__':
    ccc = CCC()
    # test()

    lvl1_parser = ccc.lvl1_parser
    lvl1_executor = ccc.lvl1_executor
    data = lvl1_parser(open("source_files/level1/level1_example.in", "r"))
    lvl1_executor(data)
