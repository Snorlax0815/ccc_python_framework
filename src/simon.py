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
