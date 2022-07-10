from turtle import Turtle, Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.fd(50)
screen=Screen()

screen.listen()
screen.exitonclick()
screen.mainloop()