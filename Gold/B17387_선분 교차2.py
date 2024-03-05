def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)


def is_two_lines_intersecting(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2

    mx1, my1 = min(x1, x2), min(y1, y2)
    mx2, my2 = max(x1, x2), max(y1, y2)
    mx3, my3 = min(x3, x4), min(y3, y4)
    mx4, my4 = max(x3, x4), max(y3, y4)

    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw123*ccw124 == 0 and ccw341*ccw342 == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4 and my3 <= my2:
            return True
    else:
        if ccw123*ccw124 <= 0 and ccw341*ccw342 <= 0:
            return True

    return 0

line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
if is_two_lines_intersecting(line1,line2):
    print(1)
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    point = []
    point.append([x1, y1])
    point.append([x2, y2])
    point.append([x3, y3])
    point.append([x4, y4])
    try:
        x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/((x1-x2)*(y3-y4)-(y1-y2)*(x3-x4))
        print(x, y)
    except:
        if point[0] > point[1]:
            point[0], point[1] = point[1], point[0]
        if point[2] > point[3]:
            point[2], point[3] = point[3], point[2]
        if point[1] == point[2]:
            print(point[1][0], point[1][1])
        elif point[0] == point[3]:
            print(point[0][0], point[0][1])
else:
    print(0)