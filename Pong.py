import turtle

wn = turtle.Screen()
wn.title("Pong by @GuiRuizz")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)


# Pontuação

pontuacao_1 = 0
pontuacao_2 = 0

#Controle 1
controle_1 = turtle.Turtle()
controle_1.speed(0)
controle_1.shape("square")
controle_1.color("white")
controle_1.shapesize(stretch_wid=5, stretch_len=1)
controle_1.penup()
controle_1.goto(-350, 0)



#Controle 2
controle_2 = turtle.Turtle()
controle_2.speed(0)
controle_2.shape("square")
controle_2.color("white")
controle_2.shapesize(stretch_wid=5, stretch_len=1)
controle_2.penup()
controle_2.goto(350, 0)


#Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = 0.2


# Caneta

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}      Player B: {}".format(pontuacao_1, pontuacao_2), align="center", font=("Montserrat", 24, "normal"))



#Funções
def controle_1_cima():
    y = controle_1.ycor()
    y += 20
    controle_1.sety(y)

def controle_1_baixo():
    y = controle_1.ycor()
    y -= 20
    controle_1.sety(y)

def controle_2_cima():
    y = controle_2.ycor()
    y += 20
    controle_2.sety(y)

def controle_2_baixo():
    y = controle_2.ycor()
    y -= 20
    controle_2.sety(y)
#Bind do Teclado

wn.listen()
wn.onkeypress(controle_1_cima, "w")  
wn.onkeypress(controle_1_baixo, "s")
wn.onkeypress(controle_2_cima, "Up")  
wn.onkeypress(controle_2_baixo, "Down")        

#Main Game Loop
while True:
    wn.update() 

    #Mover a bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    #CHECKAR A BORDA
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1  

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1   
        pontuacao_1 += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(pontuacao_1, pontuacao_2), align="center", font=("Montserrat", 24, "normal"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1  
        pontuacao_2  += 1
        pen.clear()
        pen.write("Player A: {}      Player B: {}".format(pontuacao_1, pontuacao_2), align="center", font=("Montserrat", 24, "normal"))

    #Colisão

    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() <  controle_2.ycor() + 40 and bola.ycor() > controle_2.ycor() -40):
        bola.setx(340)
        bola.dx *= -1   
    
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() <  controle_1.ycor() + 40 and bola.ycor() > controle_1.ycor() -40):
        bola.setx(-340)
        bola.dx *= -1   


        