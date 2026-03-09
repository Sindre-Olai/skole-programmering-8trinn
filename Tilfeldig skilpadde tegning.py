from tkinter import messagebox
import turtle
import random
from random import randint

skilpadde = turtle.Turtle()
s = skilpadde
s.color(random.choice(["red", "green", "yellow", "purple", "orange"]))
s.speed(5)
s.pensize(5)

turtle.bgcolor("black")

s.speed(3)

s.pendown()
for i in range((randint(5, 15))):
    s.forward(randint(10, 50))
    s.right(90)
    s.forward(randint(10, 50))
s.penup()

s.goto(-200, 100)
s.color(random.choice(["red", "green", "yellow", "purple", "orange"]))
s.pendown()
s.circle(randint(10, 100))
s.forward(50)
s.color(random.choice(["red", "green", "yellow", "purple", "orange"]))
s.forward(100)
s.turtlesize(randint(1, 5))
s.pensize(7)
s.forward(150)
s.right(90)
s.forward(75)
s.penup()

s.goto(100, -150)
s.pendown()
for i in range(randint(8, 13)):
    s.color(random.choice(["red", "green", "yellow", "purple", "orange"]))
    s.speed(8)
    s.forward(100)
    s.goto(randint(-200, 200), randint(-90, 120))
    s.right(45)
    s.forward(50)
    s.circle(randint(10, 50))
messagebox.showinfo("Information", "Tegningen er ferdig!")