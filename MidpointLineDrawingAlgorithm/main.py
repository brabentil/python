def midpoint (x_0, y_0, x_1, y_1):
    diff_x = (x_1 - x_0)
    diff_y = (y_1 - y_0)

    d = 2*diff_y - diff_x

    x = x_0
    y = y_0
    coordinates = []

    while x != x_1 & y != y_1:
        coordinates.append((x, y))
        if d < 0:
            x = x+1
            d = d + 2*diff_y
        else:
            x,y =x+1,y+1
            d = d + 2*(diff_y-diff_x)

    return coordinates


print(midpoint(2,3,8,5))