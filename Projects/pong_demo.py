import turtle

# Create the screen for the game
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("black")
sc.setup(width=1000, height=600)

#Left Paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("white")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400,0)
#Right Paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("white")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400,0)
#The Ball
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("red")
hit_ball.penup()
hit_ball.goto(-300,0)
hit_ball.dx = 5
hit_ball.dy = -5

# Initialize the score
Left_Player = 0
Right_Player = 0
 
 
# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))

# Functions to move paddle vertically and horizontally LEFT
def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)
 
 
def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)
    
# Functions to move paddle vertically and horizontally RIGHT
    
def paddlebup1():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)
 
 
def paddlebdown1():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)
  
# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "e")
sc.onkeypress(paddleadown, "x")
sc.onkeypress(paddlebup1, "Up")
sc.onkeypress(paddlebdown1, "Down")
 
 
while True:
    sc.update()
 
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)
 
    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
 
    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1
 
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        Left_Player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                      Left_Player, Right_Player), align="center",
                      font=("Courier", 24, "normal"))
 
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        Right_Player += 1
        sketch.clear()
        sketch.write("Left_player : {}    Right_player: {}".format(
                                 Left_Player, Right_Player), align="center",
                                 font=("Courier", 24, "normal"))
 
    # Paddle ball collision
    if (hit_ball.xcor() > 360 and
                        hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor()+40 and
                        hit_ball.ycor() > right_pad.ycor()-40):hit_ball.setx(360)
    hit_ball.dx*=-1
        
    if (hit_ball.xcor()<-360 and
                       hit_ball.xcor()>-370) and (hit_ball.ycor()<left_pad.ycor()+40 and
                        hit_ball.ycor()>left_pad.ycor()-40):hit_ball.setx(-360)
    hit_ball.dx*=1