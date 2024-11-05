import turtle as trtl
import random
import math

wn = trtl.Screen()

snakeBody = []
gameActive = True
pressableKeys = ["w", "a", "s", "d"]
currentLength = 0

snakeHead = trtl.Turtle()
snakeHead.shape("square")
snakeHead.fillcolor("green")
snakeHead.color("green")
snakeHead.penup()
snakeHead.speed(0)

apple = trtl.Turtle()
apple.shape("square")
apple.fillcolor("red")
apple.color("red")
apple.penup()
apple.speed(0)

def SnakeForward():
    global snakeHead
    global apple
    global wn
    snakeHead.forward(20)
    if (float(math.sqrt((snakeHead.xcor() - apple.xcor()) * (snakeHead.xcor() - apple.xcor()) + (snakeHead.ycor() - apple.ycor()) * (snakeHead.ycor() - apple.ycor()))) < 20):
       AppleHit()
    wn.ontimer(SnakeForward, 500)

def TurnSnake(event):
    global snakeHead
    if (event == "w"):
      snakeHead.setheading(90)
    elif (event == "a"):
       snakeHead.setheading(180)
    elif (event == "s"):
       snakeHead.setheading(270)
    elif (event == "d"):
       snakeHead.setheading(0)

def AppleHit():
   global apple
   apple.goto(random.randint(-150, 150), random.randint(-150, 150))
   if (apple.xcor() % 20 != 0):
      apple.setx(apple.xcor() - apple.xcor()%20)
   if (apple.ycor() % 20 != 0):
      apple.sety(apple.ycor() - apple.ycor()%20)

AppleHit()
SnakeForward()
for n in pressableKeys:
    wn.onkeypress(lambda n=n: TurnSnake(n), str(n))
wn.listen()
wn.mainloop()