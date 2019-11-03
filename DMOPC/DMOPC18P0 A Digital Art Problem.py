import sys  # p0

type = sys.stdin.readline().strip("\n")
ra, ba, ga = [float(x) for x in sys.stdin.readline().split()]
rb, bb, gb = [float(x) for x in sys.stdin.readline().split()]
part1 = float(0)
part2 = float(0)
part3 = float(0)

if type == "Multiply":
    print(ra * rb, ba * bb, ga * gb)

elif type == "Screen":
    print(1 - ((1 - ra) * (1 - rb)), 1 - ((1 - ba) * (1 - bb)), 1 - ((1 - ga) * (1 - gb)), )


elif type == "Overlay":
    if ra < .5:
        part1 = (2 * (ra * rb))
    else:
        part1 = (1 - (2 * ((1 - ra) * (1 - rb))))
    if ba < .5:
        part2 = (2 * (ba * bb))
    else:
        part2 = (1 - (2 * ((1 - ba) * (1 - bb))))
    if ga < .5:
        part3 = (2 * (ga * gb))
    else:
        part3 = (1 - (2 * ((1 - ga) * (1 - gb))))

    print(part1, part2, part3)