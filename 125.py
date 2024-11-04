import turtle as trtl

wn = trtl.Screen()

snakeBody = []
gameActive = True

snakeHead = trtl.Turtle()
snakeHead.shape("square")
snakeHead.fillcolor("green")
snakeHead.color("green")
snakeHead.penup()
snakeHead.speed(0)

def SnakeForward():
    global snakeHead
    global wn
    snakeHead.forward(20)
    wn.ontimer(SnakeForward(), 500)
SnakeForward()
wn.mainloop()