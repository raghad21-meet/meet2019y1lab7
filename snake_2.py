import turtle
import random
turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=8
time_step=100

pos_list=[]
stamp_list=[]
food_pos = []
food_stamps = []

#Go to the top of your file, and after the line that says snake.direction = “Up”,  write:
snake = turtle.clone()
snake.shape("square")

turtle.hideturtle()




#Set up positions (x,y) of boxes that make up the snake


#Hide the turtle object (it's an arrow - we don't need to see it)

#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos()
    pos_list.append(snake_pos)
    snake_stamp=snake.stamp()
    stamp_list.append(snake_stamp)
    #Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE #Draw a#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENG
    

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()
    



def remove_tail():
    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)


snake.direction="up"

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    snake.direction="up" #Change direction to up
   
    print("You pressed the up key!")


def down():
    snake.direction="down" #Change direction to up
    
    print("You pressed the down key!")

def left():
    snake.direction="left" #Change direction to up
    
    print("You pressed the left key!")

def right():
    snake.direction="right" #Change direction to up
    
    print("You pressed the right key!")


#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, "Up") # Create listener for up key

turtle.onkeypress(down, "Down")

turtle.onkeypress(left, "Left")

turtle.onkeypress(right, "Right")

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()

turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script
food = turtle.clone()
food.shape("trash.gif")
#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don't forget to hide the food turtle!
for this_food_pos in food_pos :
    food.goto(this_food_pos)
    x=food.stamp()
    food_stamps.append(x)
    food.hideturtle()
    
    
    ####WRITE YOUR CODE HERE!!
def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x,food_y)
    food_pos.append((food_x,food_y))
    y=food.stamp()
    food_stamps.append(y)
    
    



def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("you moved down!")
    elif snake.direction == "left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif  snake.direction == "right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()

    if new_y_pos <= DOWN_EDGE:
         print("You hit the down edge! Game over!")
         quit()

    if new_x_pos <= LEFT_EDGE:
         print("You hit the left edge! Game over!")
         quit()

    if new_y_pos >= UP_EDGE:
         print("You hit the up edge! Game over!")
         quit()
    if snake.pos() in pos_list:
        quit()
    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()
    #remove_tail()
    ######## SPECIAL PLACE - Remember it for Part 5
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
    else:
        remove_tail()
    if len(food_stamps)<=8:
        make_food()
    #remove the last piece of the snake (Hint Functions are FUN!)
    
    turtle.ontimer(move_snake,time_step) 


move_snake()



turtle.mainloop()
