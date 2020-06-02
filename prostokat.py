import turtle  as t 

window = t.Screen() 
turtle = t.Turtle() 
turtle.hideturtle() 

for i in range(4):
    turtle.forward(150)
    turtle.right(90)


window.mainloop() 
