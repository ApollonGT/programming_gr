import turtle

turtle.bgcolor( (0.1, 0.1, 0.3) )

t = turtle.Pen('turtle')
t.color('green')

t.backward(100)
t.left(90)
t.forward(20)
t.right(90)
t.forward(40)
t.left(90)
t.forward(20)
t.right(90)
t.forward(80)
t.right(45)
t.forward(28.3)
t.left(45)
t.forward(60)
t.right(90)
t.forward(20)
t.right(90)
t.forward(160)

t.color('red')
t.circle(20)

t.penup()
t.backward(120)
t.pendown()
t.circle(20)

t.penup()
t.goto(0,0)
