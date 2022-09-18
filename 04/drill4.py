import turtle

turtle.penup()
turtle.goto(0,-500)
turtle.pendown()

count = 6
while(count > 0):
    turtle.penup()
    turtle.goto(0,-500 + count * 100)
    turtle.pendown()
    turtle.forward(500)
    count = count - 1
    
turtle.penup()
turtle.goto(0,-500)
turtle.pendown()
turtle.right(90)

count = 6;
while(count > 0):
    turtle.penup()
    turtle.goto(-100 + count * 100, 100)
    turtle.pendown()
    turtle.forward(500)
    count = count - 1
turtle.exitonclick()
