def test():
    print("uwu")

def solve1(accel: list):

    accelWithG = [int(x) - 10 for x in accel]

    vel = 0
    height = 0
    for a in accelWithG:
        vel += a
        height += vel
    

    return height

class Drone:
    def __init__(self) -> None:
        self.h = 0
        self.v = 0
        self.a = 0
        self.acc = []
        self.debug = True

    def accel(self, accValue):
        self.a = accValue-10
        self.acc.append(accValue)
        self.v += self.a
        self.h += self.v

        if(self.debug):
            print(f"accel with {self.a}, v {self.v}, h {self.h}")

def solve3(max, h):
    print(f"max {max}, h {h}")
    d = Drone()
    d.debug = False

    print("asc")
    while d.h < h:
        d.accel(20)
    print("desc")
    while(d.h > 20):
        if d.v > -20:
            d.accel(0)
        else :
            d.accel(10)
    print(f"targeting v 0 with v {d.v}")
    while(d.v != 0):
    # if(True):
        wantedA = -d.v
        print(f"want a A of {wantedA}")

        if(wantedA < 0):
            d.accel(wantedA+10)
        else:
            if wantedA <= 10:
                d.accel(wantedA + 10)
            else:
                d.accel(20)


    print(f"starting decel with v {d.v} h {d.h}")

    d.accel(9)
    while(d.h > 0):
        d.accel(10)

    return d.acc


def solve3Old(max, h):
    print(f"max {max}, h {h}")
    currH = 0
    currV = 0
    currA = 0

    acc = []

    while currH < h:
        print("acc 20")
        currA = 10
        acc.append(currA+10)
        currV += currA
        currH += currV
        print(f"currH is {currH}")
    while(currH > 20):
        if currV > -20:

            print("acc 0")
            currA = -10
            acc.append(0)
            currV += currA
            currH += currV
            print(f"curr v {currV}, h is {currH}")
        else :
            print("acc 10 (keep steady)")
            currA = 0
            acc.append(10)
            currV += currA
            currH += currV
            print(f"curr v {currV}, h is {currH}")

    print(f"targeting v 0 with v {currV}")
    # while(currV != 0):
    if(True):
        wantedA = -currV
        print(f"want a A of {wantedA}")

        if(wantedA < 0):
            print("acc -10 (keep steady)")
            currA = 0
            acc.append(10)
            currV += currA
            currH += currV
            print(f"curr v {currV}, h is {currH}")


    print(f"starting decel with v {currV} h {currH}")



