import turtle
import time

delay = 0.1

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        head.direction = 'up'

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.sety(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.sety(x - 20)


# set up the screen
win = turtle.Screen()
win.title('Snake by @AlaBzz')
win.bgcolor('green')
win.setup(width=600, height=600)
win.tracer(0)  # turns off screen update

# create snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('black')
head.penup()  # it does not draw anything
head.goto(0, 0)
head.direction = 'stop'

# check for butts to see if they are pushed or not
win.onkeypress(move, 'Up')
win.onkeypress(move, 'Down')
win.onkeypress(move, 'Right')
win.onkeypress(move, 'Left')

# Main game loop
while True:
    win.update()
    move()
    time.sleep(delay)
win.mainloop()  # keeps the window open
