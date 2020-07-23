
import turtle

turtle.title("My Turtle Game")
turtle.bgcolor("blue")
turtle.setup(600,600)
screen = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("red")
bob.speed(99)
bob.pensize(3)

def square(size): 
  for i in range(4):
    bob.forward(size)
    bob.right(90)

def p():
  size=365
  for i in range(36):
    square(size)
    bob.right(10)
    size -= 10

p()
