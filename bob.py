import turtle

def make_head(x,y,radius,fillcolor):

    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.fillcolor(fillcolor)
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.pos(x,y)
    input()
    
make_head(30,20,100,"red")
input()

