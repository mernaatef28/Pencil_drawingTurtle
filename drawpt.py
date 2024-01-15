import turtle
import numpy as np
from PIL import Image
from skimage import measure

def get_outline_points(image_path):
    # Open the image
    img = Image.open(image_path)

    # Convert the image to grayscale for simplicity
    img_gray = img.convert('L')

    # Convert the image to a NumPy array
    img_array = np.array(img_gray)

    # Get the contours using the 'find_contours' function from skimage
    contours = measure.find_contours(img_array, 1)

    # Extract the coordinates from the contours
    outline_points = [tuple(map(int, point[::-1])) for contour in contours for point in contour]

    return outline_points

def draw_outline_with_turtle(outline_points):
    # Create a turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a turtle
    my_turtle = turtle.Turtle()
    my_turtle.speed(20)

    # Move the turtle to the starting point
    my_turtle.penup()
    my_turtle.goto(outline_points[0][0], outline_points[0][1])
    my_turtle.pendown()

    # Draw the outline
    for point in outline_points:
        my_turtle.goto(point[0], point[1])

    # Close the window on click
    screen.exitonclick()

# Example usage
image_path = "maro.png"
outline_points = get_outline_points(image_path)

# Adjust the scale of points if needed
scale_factor = 0.1
scaled_outline = [(x * scale_factor, y * scale_factor) for x, y in outline_points]

draw_outline_with_turtle(scaled_outline)
