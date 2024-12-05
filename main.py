import turtle

screen = turtle.Screen()
screen.bgcolor('lightpink')

t=turtle.Turtle()

t.penup()
t.goto(0,200)
t.pendown()
t.write("All About Me", font=("Arial", 35, "bold"), align="center")
t.penup()
t.goto(0,-50)
t.pendown()
t.write("Ellie Schrader", font=("Arial", 35, "bold"), align="center")
t.penup()
t.goto(0,-300)
t.pendown()
t.pensize(5)
t.pencolor('powder blue')
t.fillcolor('powder blue')
t.begin_fill()
t.circle(87)
t.end_fill()
t2=turtle.Turtle()
t2.penup()
turtle.addshape("penguin.gif")
t2.shape("penguin.gif")
t2.goto(100,100)
a=t2.stamp()

t2.penup()
turtle.addshape("tree.gif")
t2.shape("tree.gif")
t2.goto(-100,100)
a=t2.stamp()
enter=input("Press Enter to Start")
t.clear()
t2.clearstamps()
t2.hideturtle()

screen.bgcolor('orange')
t.penup()
t.goto(0,200)
t.pendown()
t.write("My Favorite Foods", font=("Arial", 35, "bold"), align="center")
t.penup()
t.goto(-160,40)
t.write("Mac & Cheese", font=("Arial", 20, "bold"), align="center")
t.penup()
t.goto(0,40)
t.write("tacos", font=("Arial", 20, "bold"), align="center")
t.penup()
t.goto(140,40)
t.write("Pizza", font=("Arial", 20, "bold"), align="center")
t.penup()
t.goto(-75, 105)
t.fillcolor('purple')
t.pendown()
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.end_fill()

t2.penup()
turtle.addshape("pizza.gif")
t2.shape("pizza.gif")
t2.goto(100,-100)
a=t2.stamp()

t2.penup()
t2.goto(-100,-100)
turtle.addshape("mac.gif")
t2.shape("mac.gif")
t2.goto(-100,-100)
a=t2.stamp()
t2.goto(-100,-200)


enter=input("Press Enter to go to next slide")
t.clear()
t2.clearstamps()
t2.hideturtle()

screen.bgcolor('powder blue')
t.pencolor('black')
t.penup()
t.goto(0,200)
t.pendown()
t.write("My Hobbies", font=("Arial", 35, "bold"), align="center")
t.penup()
t.penup()
t.goto(-250,40)
t.write("Dance", font=("Arial", 15, "bold"), align="center")
t.penup()
t.goto(-150,40)
t.write("Baking", font=("Arial", 15, "bold"), align="center")
t.penup()
t.goto(-40,40)
t.write("Writing", font=("Arial", 15, "bold"), align="center")
t.penup()
t.goto(140,40)
t.write("Hanging out with friends", font=("Arial", 15, "bold"), align="center")
t.penup()
t.pencolor('black')
t.fillcolor('pink')
t.begin_fill()
t.goto(-50,-10)
t.pendown()
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.end_fill()
t2.penup()
turtle.addshape("dance.gif")
t2.shape("dance.gif")
t2.goto(100,-200)
a=t2.stamp()


t2.penup()
turtle.addshape("shop.gif")
t2.shape("shop.gif")
t2.goto(-100,-200)
a=t2.stamp()
t2.goto(-100,-200)

enter=input("Press Enter to go to next slide")
t.clear()
t2.clearstamps()
t2.hideturtle()

screen.bgcolor('medium slate blue')
t.penup()
t.goto(0,200)
t.pendown()
t.write("My Favorite Movie", font=("Arial", 35, "bold"), align="center")
t.penup()
t.goto(-10,100)
t.pencolor('green')
t.fillcolor('green')
t.penup()
t.goto(-10,100)
t.pencolor('blue')
t.fillcolor('orange')
t.pendown()
t.begin_fill()
t.circle(30,180)
t.end_fill()
t.penup()
t.goto(0,-50)
t.pendown()
t.pencolor("black")
t.write("Ant Man", font=("Arial", 35, "bold"), align="center")

t2.penup()
turtle.addshape("ant.gif")
t2.shape("ant.gif")
t2.goto(100,-200)
a=t2.stamp()


t2.penup()
turtle.addshape("movie.gif")
t2.shape("movie.gif")
t2.goto(-100,-200)
a=t2.stamp()
t2.goto(-100,-200)
enter=input("Press Enter to go to next slide")
t.clear()
t2.clearstamps()
t2.hideturtle()

screen.bgcolor('pale green')
t.penup()
t.goto(0,200)
t.pendown()
t.write("My Favorite Sport", font=("Arial", 35, "bold"), align="center")
t.penup()
t.goto(0,-50)
t.pendown()
t.write("Dance", font=("Arial", 35, "bold"), align="center")
t.penup()
t.goto(60,10)
t.fillcolor('blue')
t.pendown()
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t2.penup()
turtle.addshape("odance.gif")
t2.shape("odance.gif")
t2.goto(100,-200)
a=t2.stamp()


t2.penup()
turtle.addshape("twodance.gif")
t2.shape("twodance.gif")
t2.goto(-100,-200)
a=t2.stamp()
t2.goto(-100,-200)

enter=input("Press Enter to go to next slide")
t.clear()
t2.clearstamps()