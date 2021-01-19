import turtle
import time
import random 
def pantalla_inicio():
    pantalla = turtle.Screen()
    pantalla.title("Miniproyecto 1 - Snake Game")
    pantalla.bgcolor("#000000")
    pantalla.setup(width=800,height=600)
    pantalla.tracer()
    #escuchar el teclado 
    return pantalla


def zona_juego():
    marco = turtle.Turtle("square")
    marco.color("#ffffff","#828282")
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

def marcador():
    pizarra = turtle.Turtle() 
    pizarra.speed(0) 
    pizarra.shape("square") 
    pizarra.color("#f8f900") 
    pizarra.penup() 
    pizarra.hideturtle() 
    pizarra.goto(0, 250) 
    pizarra.write("Score : 0  High Score : 0", align="center", font=("Comic Sans MS", 24, "bold"))
    return pizarra

def arriba(): 
    if serpiente.direction != "down": 
        serpiente.direction = "up"
    pass
  
def abajo(): 
    if serpiente.direction != "up": 
        serpiente.direction = "down"
    pass
  
def izq(): 
    if serpiente.direction != "right": 
        serpiente.direction = "left"
    pass
  
def derch(): 
    if serpiente.direction != "left": 
        serpiente.direction = "right"
    pass

def v_direccion():
    global serpiente
    if serpiente.direction == "up":
        serpiente.sety( serpiente.ycor()+20 )
        pass
    if serpiente.direction == "down":
        serpiente.sety( serpiente.ycor()-20 )
        pass
    if serpiente.direction == "right":
        serpiente.setx( serpiente.xcor()+20 )
        pass
    if serpiente.direction == "left":
        serpiente.setx( serpiente.xcor()-20 )
        pass
    pass

def comida():
    comida = turtle.Turtle() 
    comida.speed(0) 
    comida.shape("circle") 
    comida.color("#ff1e0b") 
    comida.penup() 
    comida.goto(0, 100) 
    return comida

def reset():
    global serpiente, manzana, cola, score, retraso, pizarra
    time.sleep(1)
    serpiente.hideturtle() 
    serpiente.goto(0, 0) 
    serpiente.direction = "Stop"
    serpiente.showturtle()

    comer_manzana()
    for colas in cola: 
        colas.goto(1000, 1000) 
    cola.clear() 
    score = 0
    retraso = 0.1
    pizarra.clear() 
    pizarra.write("Score : {} High Score : {} ".format( 
            score, high_score), align="center", font=("Comic Sans MS", 24, "bold"))
    pass

def dibujar_cuerpo():
    for i in range(len(cola)-1, 0, -1): 
        x = cola[i-1].xcor() 
        y = cola[i-1].ycor() 
        
        cola[i].goto(x, y)
        cola[i].showturtle() 
    if len(cola) > 0: 
        x = serpiente.xcor() 
        y = serpiente.ycor()
        
        cola[0].goto(x, y)
        cola[0].showturtle()
    pass 

def comer_manzana():
    global manzana, retraso, cola, pizarra, score, high_score

    #aumentar marcador
    score += 10
    if score > high_score: 
        high_score = score 
    pizarra.clear() 
    pizarra.write("Score : {} High Score : {} ".format( score, high_score), align="center", font=("Comic Sans MS", 24, "bold"))

    #añadir nueva parte al cuerpo
    nueva_parte_cola = turtle.Turtle("square")
    nueva_parte_cola.hideturtle() 
    nueva_parte_cola.speed(0) 
    nueva_parte_cola.color("#00f596")  # cola colour 
       # nueva_parte_cola.shapesize(10 / 20 )
    nueva_parte_cola.penup() 
    cola.append(nueva_parte_cola)
     #aumentar velocidad   
    retraso = retraso / (2*(len(cola)))
    #if len(cola) > 5:
    #   retraso = 0.0001
    manzana.hideturtle()
    x = random.randint(-200, 200) 
    y = random.randint(-200, 200) 
    manzana.goto(x, y)
    manzana.showturtle()
    pass

#variables globales
snake_cola =[[0,0]]
cola = []
score = 0
high_score = 0
serpiente = turtle.Turtle("square")
serpiente.color("#008f58")
#serpiente.shapesize(10 / 20 )
serpiente.penup()
serpiente.home()
serpiente.direction = "Stop"
retraso = 0.1

pantalla = pantalla_inicio()
#escuchar el teclado

pantalla.listen()
pantalla.onkeypress(arriba, "Up") 
pantalla.onkeypress(abajo, "Down") 
pantalla.onkeypress(izq,"Left") 
pantalla.onkeypress(derch, "Right") 
    
zona_juego()
pizarra= marcador()
manzana=comida()

while True: 
    pantalla.update()

    #Colision contra marco
    if serpiente.xcor() > 340 or serpiente.xcor() < -340 or serpiente.ycor() > 240 or serpiente.ycor() < -240: 
        reset()
       # pen.clear() 

    #colision contra manzana
    if serpiente.distance(manzana) < 20: 
        comer_manzana()

    #dibuja cola si la tiene    
    dibujar_cuerpo()
    #movimiento
    v_direccion()

    #colision contra cuerpo
    for colas in cola: 
        if colas.distance(serpiente) < 20:
            reset()
    
    time.sleep(retraso)  

pantalla.mainloop()