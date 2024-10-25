from simon import solve1, solve3, test


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
            outputs.append(line)
        print(outputs)
        return [max_time,outputs]

    def lvl3_executor(self, data):
        max_time = int(data[0])
        heights = [int(h.strip()) for h in data[1]]
        out = []
        for h in heights:
            res = solve3(max_time, h)
            print(res)
            res = [str(x) for x in res]
            out.append(" ".join(res))
        return "\n".join(out)






if __name__ == '__main__':
    ccc = CCC()
    # test()

    lvl3_parser = ccc.lvl3_parser
    lvl3_executor = ccc.lvl3_executor
    data = lvl3_parser(open("source_files/level3/level3_example.in", "r"))
    lvl3_executor(data)
