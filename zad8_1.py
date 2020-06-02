import turtle  as t # korzystamy z pliku turtle.py

window = t.Screen() # tworzy nam okno programu
turtle = t.Turtle() # tworzymy element na którym bedziemy rysować
turtle.hideturtle() # usuwa grot strzałki
turtle.forward(50) # rysuje nam 50 pikseli prosto
turtle.right(90) # obrót o 90 stopni
turtle.forward(50)
turtle.right(90) # obrót o 90 stopni
turtle.forward(50)
turtle.right(90) # obrót o 90 stopni
turtle.forward(50)
window.mainloop() # okno nam się nie zamyka
# turtle.getscreen()._root.mainloop() # gdy nie działa linijka wyżej