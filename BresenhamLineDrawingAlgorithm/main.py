import matplotlib.pyplot as plt



def bresenham_line(x1, y1, x2, y2):
    points = []

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        points.append((x1, y1))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    return points


# Example usage
x1, y1, x2, y2 = 2, 3, 10, 7  # Change these values as needed
points = bresenham_line(x1, y1, x2, y2)

# Plot the line
x_vals, y_vals = zip(*points)
plt.plot(x_vals, y_vals, marker="o", color="black", linestyle="None")
plt.xlim(0, max(x1, x2) + 2)
plt.ylim(0, max(y1, y2) + 2)
plt.gca().invert_yaxis()  # Invert y-axis to match computer graphics coordinates
plt.grid()
plt.show()
