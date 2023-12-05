import turtle # module that allows you to do basic graphics (built in)
import winsound

# we create a window
wn = turtle.Screen() 
wn.title("pong") # title of screen
wn.bgcolor("black") # background color of window
wn.setup(width=800, height=600) # dimentions of window
wn.tracer(0) # to stop window from updating

# to keep track of the score

score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle() # turtle object
paddle_a.speed(0) # speed of animation
paddle_a.shape("square") # shape
# by default the square shape is 20x20
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # (20x5 and 20x1) ---> (100 and 20)
paddle_a.color("white")
paddle_a.penup() # no drawing while moving
paddle_a.goto(-350, 0) # center - left of the screen

# paddle B
paddle_b = turtle.Turtle() # turtle object
paddle_b.speed(0) # speed of animation
paddle_b.shape("square") # shape
# by default the square shape is 20x20
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # (20x5 and 20x1) ---> (100 and 20)
paddle_b.color("white")
paddle_b.penup() # no drawing while moving
paddle_b.goto(350, 0) # center - left of the screen

# ball

ball = turtle.Turtle() #turtle object
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

# pen (to write scoring)
pen = turtle.Turtle()
pen.speed(0) #animation speed
pen.color("white")
pen.penup() #no drawing when moving
pen.hideturtle() #to keep pen hidden  
pen.goto(0, 260)
pen.write("Player A: 0 || Player B: 0", align="center", font=("Courier", 15, "normal"))

# movement (movement by pixel)

ball.dx = 0.08 # delta x - x speed
ball.dy = 0.08 # delta y 

# functions

def paddle_a_up():
    y = paddle_a.ycor() # returns the y values from the paddle_a object (part of tortule)
    y += 20 # add 20 to y
    paddle_a.sety(y) #set y to the new y

def paddle_a_down():
    y = paddle_a.ycor() #returns the y vallues from the paddle_a object
    y -= 20
    paddle_a.sety(y) 

def paddle_b_up():
    y = paddle_b.ycor() # returns the y values from the paddle_a object (part of tortule)
    y += 20 # add 20 to y
    paddle_b.sety(y) #set y to the new y

def paddle_b_down():
    y = paddle_b.ycor() #returns the y vallues from the paddle_a object
    y -= 20
    paddle_b.sety(y) 

# keyboard binding

wn.listen() #to listen two keyboard input
wn.onkeypress(paddle_a_up, "w") #when user presses w, call the function paddle_a_up
# the object will therefore move 20 pixels up
wn.onkeypress(paddle_a_down, "s")
#wn.onkeypress(paddle_b_up, "Up") 
#wn.onkeypress(paddle_b_down, "Down")

# main game loop

while True :
    wn.update() #everytime the loop runs it updates the screen

    # move the ball 
    ball.setx(ball.xcor() + ball.dx) # get the x coord and add dx to it 
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    # remember the dimentions (800 x 600)

    if ball.ycor() > 290: 
            ball.sety(290)
            ball.dy *= -1 # to reverse direction
            winsound.PlaySound("col.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290: 
            ball.sety(-290)
            ball.dy *= -1 # to reverse direction
            winsound.PlaySound("col.wav", winsound.SND_ASYNC)
    
    if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1
            winsound.PlaySound("point.wav", winsound.SND_ASYNC) #async so when the sound plays it doesn't stop the program
            score_a += 1 # for scoring
            pen.clear() # to clear what's writen and update
            pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "normal"))
    
    if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1
            winsound.PlaySound("point.wav", winsound.SND_ASYNC)
            score_b += 1
            pen.clear() # to clear what's writen and update
            pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align="center", font=("Courier", 15, "normal"))

    # paddle and ball collisions

    # coords of paddle_a are (-350, 0)
    # coords of paddle_b are (350, 0)
    # each figure is 20px wide by 100px tall

    # coords of collision paddle_b: 
    # at whatever coord the paddle is, add it 40 up and 40 down
    # the ball has to fall into that range with: 
    # ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50 (could also be +40 and -40 respectively)
    # the x will just be ball.xcor() > 340 and ball.xcor() < 350

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340) # bounce back to the left a bit
        ball.dx *= -1
        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)

    # paddle_a 

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340) # bounce back to the right a bit
        ball.dx *= -1
        winsound.PlaySound("pong.wav", winsound.SND_ASYNC)

    # AI player

    # a workaround so the AI paddle doesn't glitch out is to add another condition
    # if paddle b y cord is lesser than ball y cord AND the absolute number of their difference is bigger than 10
    if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_up()
    elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_down()