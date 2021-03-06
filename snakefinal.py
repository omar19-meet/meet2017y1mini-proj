import turtle
import random
import pygame
turtle.tracer(1,0)

#---Setup---#
SIZE_X=800
SIZE_Y=500
turtle.penup()
turtle.setup(SIZE_X,SIZE_Y)

edge=turtle.clone()

edge.penup()
edge.shape("turtle")
edge.goto(-(SIZE_X/2)+1,SIZE_Y/2-1)
edge.pendown()
edge.goto(SIZE_X/2-1,SIZE_Y/2-1)
edge.goto(SIZE_X/2-1,-(SIZE_Y/2)+1)
edge.goto(-(SIZE_X/2)+1,-(SIZE_Y/2)+1)
edge.penup()
edge.hideturtle()

#---Variables----#
direction = 0
UP_EDGE=250
DOWN_EDGE=-250
RIGHT_EDGE=400
LEFT_EDGE=-400

UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR="space"

SQUARE_SIZE=20
START_LENGTH=1

snake=turtle.clone()
snake.shape("square")

turtle.register_shape("trash.gif")
food=turtle.clone()
food.shape("trash.gif")

UP=0
LEFT=1
DOWN=2
RIGHT=3

score=0

#---Lists---#
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamps=[]

#---Body of Snake---#
for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)

    bodystamp=snake.stamp()
    stamp_list.append(bodystamp)

#---Functions---#
#The Following functions move the snake to different directions using the direction variable
def up():
    global direction
    direction=UP
    print("You pressed the up key!")

def left():
    global direction
    direction=LEFT
    print("You pressed the left key!")

def down():
    global direction
    direction=DOWN
    print("You pressed the down key!")

def right():
    global direction
    direction=RIGHT
    print("You pressed the right key!")
#This function randomizes food on the map
def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    my_food=(food_x,food_y)
    food_pos.append(my_food)
    new_food_stamp=food.stamp()
    food_stamps.append(new_food_stamp)
#This function moves the snake
def move_snake():
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    
    global direction
    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print("You moved up!")
    elif direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)

        print("You moved down!")

    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)


    global food_stamps, food_pos

    if snake.pos() in food_pos:
        global score
        turtle.goto(-380,230)
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)        
        print("You have eaten the food!")
        turtle.clear()
        score+=1
        turtle.write(score)
        make_food()
    else:
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
            
        
    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]
    newpostwice=(new_pos, new_pos)
    if new_x_pos>=RIGHT_EDGE:
        print("You hit the right edge! Game OVER!")
        quit()
    elif new_x_pos<=LEFT_EDGE:
        print("You hit the left edge! Game OVER!")
        quit()
    elif new_y_pos>=UP_EDGE:
        print("You hit the top edge! Game OVER!")
        quit()
    elif new_y_pos<=DOWN_EDGE:
        print("You hit the bottom edge! Game OVER!")
        quit()
    if pos_list[-1]in pos_list[0:-1]:
        print("You hit yourself! Game OVER!")
        quit()


    turtle.ontimer(move_snake,TIME_STEP)

#---Start---#
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()
turtle.hideturtle()
make_food()
move_snake()

