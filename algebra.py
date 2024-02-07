import turtle
import numpy as np

def getScalingFactor(points):
    x_range = abs(points[0][0] - points[-1][0])
    y_values = [point[1] for point in points]
    y_range = abs(max(y_values) - min(y_values))
    scalingFactor = 400/max(x_range,y_range)
    return scalingFactor


def plot_points(points ,color="black"):
    scalingFactor = getScalingFactor(points)
    screen = turtle.Screen()
    my_turtle = turtle.Turtle()
    my_turtle.shape("circle")  # Set the shape of the turtle to a circle for stamping
    my_turtle.shapesize(.5)
    my_turtle.color(color)
    my_turtle.speed(1000)

    for point in points:
        x, y = point
        my_turtle.penup()   # Lift the pen so it doesn't draw lines when moving to the point
        my_turtle.goto(x * scalingFactor -250, y * scalingFactor -250)  # Move the turtle to the specified point
        my_turtle.stamp()    # Stamp a circle at the current position

    turtle.done()

def lagrangify(start, numPoints, stop, originalPoints):
    x_values = [start + i * (stop - start) / (numPoints - 1) for i in range(numPoints)]
    points = [[x, lagrange_interpolation(originalPoints, x)] for x in x_values]
    return points

def lagrange_interpolation(points, x):
    def basis(i, x_point):
        terms = []
        for j in range(len(points)):
            if j != i:
                terms.append((x - points[j][0])/(points[i][0] - points[j][0]))

        return np.prod(terms)

    return sum(points[i][1] * basis(i, x) for i in range(len(points)))

# Example usage
points = [(0, 1), (1, 3), (2, 7), (3, 5), (4, 1), (5, 10), (6,15), (7,5), (8,1)]  # Example points
plot = lagrangify(0,200,8,points)
plot_points(plot)