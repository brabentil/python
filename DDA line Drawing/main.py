def dda(x0, y0, x1, y1):
    xDiff = x1 - x0
    yDiff = y1 - y0
    steps = max(abs(xDiff), abs(yDiff))
    xInc = xDiff / steps
    yInc = yDiff / steps
    x, y = x0, y0

    points = []

    for i in range(steps + 1):
        points.append((round(x), round(y)))
        x += xInc
        y += yInc

    return points

print(dda(1,7,11,17))