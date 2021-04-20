import turtle              # imports turtle

pen = turtle.Turtle()      #creates an instance of turtle called pen
# pen.fd(100)                   # pen will move forwards
# pen.bk(100)                   # pen will move backwards
# pen.lt(angle)              # turns left default 90
# pen.rt(angle)              # turns right default 90
pen.pu()                   # pen up
pen.goto(-350, -300)
pen.pd()                   # pen down
# pen.setheading(180)     # sets the direction (180 is left)
pen.speed(10)               # sets the draw speed, (1–10)


def draw_triangle(length):
    pen.setheading(180)
    for i in range(3):
        pen.rt(120)
        pen.fd(length)


def draw_triangele_two_normal(length):
    draw_triangle(length)
    pen.rt(120)
    pen.fd(length)
    draw_triangle(length)
    pen.lt(120)
    pen.fd(length)
    draw_triangle(length)
    pen.fd(length)


def draw_triangele_two(length, order):
    if order == 1:
        draw_triangle(length)
    else:
        draw_triangele_two(length, order-1)
        pen.rt(120)
        pen.fd(length)
        draw_triangele_two(length, order-1)
        pen.lt(120)
        pen.fd(length)
        draw_triangele_two(length, order-1)
        pen.fd(length)


def draw_triangele_three(length, order):
    if order == 1:
        draw_triangle(length)
    else:
        draw_triangele_three(length, order-1)
        pen.rt(120)
        pen.fd(length * (order-1))
        draw_triangele_three(length, order-1)
        pen.lt(120)
        pen.fd(length * (order-1))
        draw_triangele_three(length, order-1)
        pen.fd(length * (order-1))


def draw_triangele_n(length, order):
    if order == 1:
        draw_triangle(length)
    else:
        draw_triangele_n(length, order-1)
        pen.rt(120)
        pen.fd(length * 2 ** (order-2))
        draw_triangele_n(length, order-1)
        pen.lt(120)
        pen.fd(length * 2 ** (order-2))
        draw_triangele_n(length, order-1)
        pen.fd(length * 2 ** (order-2))


def tri_force(length, order):
    factor = 2 ** (order - 1)
    length = length / factor
    draw_triangele_n(length, order)


window = turtle.Screen()
# tri_force(700, 4)
window.exitonclick()




