# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl 
import random 

#-----game configuration----
shape = "turtle"
size = 2
color = "darkred"
score = 0 

font_setup = ("impact", 20, "normal")
timer = 7
counter_interval = 1000   #1000 represents 1 second
timer_up = False


#-----initialize turtle-----
oni = trtl.Turtle(shape = shape)
oni.color(color)
oni.shapesize(size)
oni.speed(-3)

score_writer = trtl.Turtle()
score_writer.ht()
score_writer.penup()
score_writer.goto(-390, 290)
font = ("impact", 35, "bold")
score_writer.write(score, font=font)

counter =  trtl.Turtle()
counter.ht()
counter.penup()
counter.goto(294, -293)



#-----game functions--------
def turtle_clicked(x,y):  
    print("oni was clicked D:")
    change_position()
    score_counter()


def change_position():
    oni.penup()
    oni.ht()
    new_xpos = random.randint(-400, 400)
    new_ypos = random.randint(-300, 300)
    oni.goto(new_xpos, new_ypos)
    oni.st()

def score_counter():
    global score
    score += 1
    print(score)
    score_writer.clear()
    score_writer.speed(0)
    score_writer.write(score, font=font)


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    gameover()
    counter.write("GG Go again", font=font_setup)
    timer_up = True
    
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 


def gameover():
    wn.bgcolor("teal") #change the BG color

    oni.ht()
    oni.goto(500, 500)
    counter.goto(0, 0)




#-----events----------------
oni.onclick(turtle_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval) 
wn.bgcolor("lightblue")
wn.mainloop()