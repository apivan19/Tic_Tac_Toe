# Program Overview: 
# Written in Python 3.7
# Creates a Window with some shapes that do things as specified in the code below...
# Three of the circles move around diagonally and will switch off depending on which of the other circles you press.
# (i.e. if you press, the red circle, the black circle will move / randomize direction, if  you press the black circle, the yellow circle will start moving / randomize direction, etc)
# One Circle will simply move to where ever you click if you don't click on another shape
# If you click inside that one circle, it will go back to the middle of the screen
# This program has an exit button as well as two buttons that will adjust the speed of the moving circles 

from graphics import *
import random
import time
import math

# This function takes in a point and a square and returns True if you clicked on it
def squareclicked(point, square):
    # Get the X and Y coords where clicked
    x, y = point.getX(), point.getY()

    # Get the bounds of the square
    x1 = square.getP1().getX()
    x2 = square.getP2().getX()
    y1 = square.getP1().getY()
    y2 = square.getP2().getY()

    # If clicked between the two points return True
    return x1 < x < x2 and y1 < y < y2


# This function takes in a point and a circle and returns True if you clicked on it
def circleclicked(point, circle):
    # Determine the coords of point and circle
    x, y = point.getX(), point.getY()
    circle_radius = circle.getRadius()
    circle_center = circle.getCenter()
    circle_center_x = circle_center.getX()
    circle_center_y = circle_center.getY()
    # Calculate the distance
    distance = math.sqrt((circle_center_x - x) ** 2 + (circle_center_y - y) ** 2)
    # If distance < radius: you clicked within the circle
    return distance < circle_radius


def create_shapes():

    # List of colors that the square can be
    colors = [
        "green",
        "pink",
        "yellow",
        "cyan",
        "orange",
    ]

    # Create the graphics window
    win = GraphWin("Shapes_n_Buttons", win_x_size, win_y_size)
    win.setBackground("gold")

    # Draw the black circle and make sure it doesn't spawn outside the boundaries of the window
    black_circle = Circle(
        Point(
            random.randrange(circle_radius, win_x_size - circle_radius),
            random.randrange(circle_radius, win_y_size - circle_radius),
        ),
        circle_radius,
    )
    black_circle.setFill("black")

    # Make the red circle and make sure it doesn't spawn outside the boundaries of the window
    red_circle = Circle(
        Point(
            random.randrange(circle_radius, win_x_size - circle_radius),
            random.randrange(circle_radius, win_y_size - circle_radius),
        ),
        circle_radius,
    )
    red_circle.setFill("red")

    # Make a circle with a random color
    rand_color_circle = Circle(
        Point(
            random.randrange(circle_radius, win_x_size - circle_radius),
            random.randrange(circle_radius, win_y_size - circle_radius),
        ),
        circle_radius,
    )
    rand_color_circle.setFill(random.choice(colors))

    # Make the circle that moves to where you click when you don't click on another shape - Always spawns in the middle of the window
    point_circle = Circle(Point(win_x_size / 2, win_y_size / 2), circle_radius)
    point_circle.setFill("blue")
    point_circle.setWidth(10)
    point_circle.setOutline("red")

    # Make an exit button and its label
    exit_button = Rectangle(Point(715, 5), Point(795, 45))
    exit_button.setFill("white")
    exit_text = Text(Point(755, 25), "EXIT")

    # Make an speed buttons and their labels
    faster_button = Rectangle(Point(25, 5), Point(75, 35))
    faster_button.setFill("green")
    slower_button = Rectangle(Point(25, 45), Point(75, 75))
    slower_button.setFill("orange")

    faster_text = Text(Point(50 , 20), "^")
    slower_text = Text(Point(50 , 60), "\/")

    return (
        win,
        black_circle,
        red_circle,
        rand_color_circle,
        point_circle,
        exit_button,
        exit_text,
        faster_button,
        faster_text,
        slower_button,
        slower_text
    )

# Draw what needs to be drawn
def draw(objects):
    for thing in objects[1:]:
        thing.draw(objects[0])


# The bounce function accepts a circle as an argument, as well as the change in x, and the change in y
#    and checks to see if the movement of the circle will take it outside the graphics window.
#    Inverts the sign (direction) if yes
def bounce(circle, dx, dy):
    radius = circle.getRadius()
    x, y = circle.getCenter().getX(), circle.getCenter().getY()
    if x + dx < radius or x + dx > win_x_size - radius:
        dx *= -1
    if y + dy < radius or y + dy > win_y_size - radius:
        dy *= -1
    return dx, dy


def main():

    # Call the create_shapes_function to make the shapes
    (
        win,
        black_circle,
        red_circle,
        rand_color_circle,
        point_circle,
        exit_button,
        exit_text,
        faster_button,
        faster_text,
        slower_button,
        slower_text
    ) = create_shapes()

    # Call the draw() function to draw all the objects
    draw(
        [
            win,
            black_circle,
            red_circle,
            rand_color_circle,
            point_circle,
            exit_button,
            exit_text,
            faster_button,
            faster_text,
            slower_button,
            slower_text
        ]
    )

    # Set start time to a variable
    start_time = time.time()

    # Give the initial direction (random) and speed (10) to the black_circle while the other shapes stay still
    dx, dy = (random.choice([1, -1])), (random.choice([1, -1]))
    currently_moving = black_circle

    # While loop continues until 60 seconds have passed and then closes the window
    time_limit = 60

    # Initial Speed of Circles
    speed = 10
    
    while (time_limit - (time.time() - start_time)) > 0:

        # Update the Timer every 0.1 seconds
        timer = Text(
            Point(win_x_size / 2, 25),
            f"Time Remaining: {int(time_limit - (time.time() - start_time))}",
        )
        timer.draw(win)
        time.sleep(0.1)
        timer.undraw()

        # Moves the object that is set to be currently moving
        currently_moving.move(dx*speed, dy*speed)

        # Checks for user click
        point = win.checkMouse()

        # If there was a click, check if one of the shapes was clicked
        if point:
            # If the black_circle was clicked, moving_object becomes the red_circle (if it wasn't already) and it's direction randomizes
            if circleclicked(point, black_circle):
                dx, dy = (random.choice([1, -1])) * speed, (random.choice([1, -1])) * speed
                currently_moving = red_circle
            # If the red_circle was clicked, moving_object becomes the square (if it wasn't already) and it's direction randomizes
            elif circleclicked(point, red_circle):
                dx, dy = (random.choice([1, -1])) * speed, (random.choice([1, -1])) * speed
                currently_moving = rand_color_circle
            # If the square was clicked, moving_object becomes the black_square (if it wasn't already) and it's direction randomizes
            elif circleclicked(point, rand_color_circle):
                dx, dy = (random.choice([1, -1])) * speed, (random.choice([1, -1])) * speed
                currently_moving = black_circle
            # If the exit button is clicked, exit
            elif squareclicked(point, exit_button):
                win.close()

            # If the speed buttons are pressed, mess with the speed!
            elif squareclicked(point, faster_button):
                print("faster")
                speed *= 2
            elif squareclicked(point, slower_button):
                print("slower")
                speed /= 2

            # If none of the other shapes was clicked:
            else:
                # Calculate the distance that you want to move the circle by
                circle_position = point_circle.getCenter()
                move_dx = (circle_position.getX() - point.getX()) * -1
                move_dy = (circle_position.getY() - point.getY()) * -1

                # How smooth the movement should be (Higher, the smoother)
                smoothness = 500
                # If I click within the blue circle, it will return back to the middle
                if math.sqrt(move_dx ** 2 + move_dy ** 2) < circle_radius:
                    for i in range(smoothness):
                        point_circle.move(
                            (win_x_size / 2 - circle_position.getX()) / smoothness,
                            (win_y_size / 2 - circle_position.getY()) / smoothness,
                        )
                # If I click outside the blue circle, the circle moves to where I click
                else:
                    # I could have done just .move(), but it isn't very smooth....
                    for i in range(smoothness):
                        point_circle.move(move_dx / smoothness, move_dy / smoothness)

        dx, dy = bounce(currently_moving, dx, dy)

    # When time runs out, close the graphics window
    win.close()


# Make these into global variables because it's annoying having to send them between functions
win_x_size, win_y_size = 800, 800

# The radius for all circles in this program
circle_radius = 30

# Run this is a script
if __name__ == "__main__":
    main()
