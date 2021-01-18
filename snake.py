import turtle
def pantalla_inicio():
    screen = turtle.Screen()
    screen.title("Miniproyecto 1 - Snake Game")
    screen.bgcolor("#000000")
    screen.setup(width=800,height=600)
    screen.tracer()   
    pass

def zona_juego():
    marco = turtle.Turtle("square")
    marco.color("#ffffff","gray")
    marco_coor = ((0, -250),(-350,-250),(-350,250),(0,250),(350,250),(350,0),(350,-250),(0,-250))
    marco.penup()
    marco.hideturtle()
    marco.goto(marco_coor[0])
    marco.pendown()
    marco.pensize(5)
    marco.speed(0)
    marco.begin_fill()
    for i in marco_coor:
        marco.goto(i)
    marco.end_fill()
    pass
pantalla_inicio()
zona_juego()
pen = turtle.Turtle("square")
pen.color("#ffffff")
pen.shapesize(10 / 20 )
pen.penup()

turtle.done()