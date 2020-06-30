"""
--------------------------
Нажмите Escape для выхода
--------------------------
"""
from turtle import Turtle, Screen

clr = (64, 64, 64)
text_list = ['R', 'G', 'B', '', 90, -60, -210, 250]
cl_list = ['red', 'green', 'blue', 150, 0, -150]

screen = Screen()
screen.delay(0)
screen.title('Миксер цветов')
screen.colormode(255)

cl_r = Turtle(shape='circle')
cl_g = cl_r.clone()
cl_b = cl_r.clone()

for t, turtle in enumerate(screen.turtles()):
    turtle.speed(0)
    turtle.shapesize(3, 3, 5)
    turtle.color(cl_list[t])
    turtle.width(10)
    turtle.pu()
    turtle.setpos(-255, cl_list[3 + t])
    turtle.pd()
    turtle.setx(255)
    turtle.pu()
    turtle.setx(0)
    turtle.pencolor(clr)

for obj in range(4):
    text = Turtle()
    text.color(clr)
    text.hideturtle()
    text.pu()
    text.sety(text_list[-4 + obj])
    text.write(text_list[obj], align="center", font=("Arial", 16, ("bold", "italic")))


def goto_r(x1, y1):
    y1 = 150
    cl_r.goto(max(-255, min(x1, 255)), y1)


def goto_g(x2, y2):
    y2 = 0
    cl_g.setposition(max(-255, min(x2, 255)), y2)


def goto_b(x3, y3):
    y3 = -150
    cl_b.setpos(max(-255, min(x3, 255)), y3)


def stop():
    screen.bye()


def main():
    global r, g, b
    cl_r.ondrag(goto_r)
    cl_g.ondrag(goto_g)
    cl_b.ondrag(goto_b)

    r = int(round((cl_r.xcor() + 255) / 2.))
    g = int(round((cl_g.xcor() + 255) / 2.))
    b = int(round((cl_b.xcor() + 255) / 2.))
    screen.bgcolor(r, g, b)

    text.clear()
    text.write((r, g, b), align="center", font=("Arial", 22, 'bold'))

    screen.ontimer(main, 120)


screen.onkeypress(stop, 'Escape')
screen.listen()

main()
screen.mainloop()
print(f'R={r}, G={g}, B={b}')
