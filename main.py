from turtle import Screen,Turtle
import time
from snake import Snake
from snake_food import Food
from snake_score import Score
screen = Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.listen()
screen.title("MY SNAKE GAME")
screen.tracer(0)
my_snake = Snake()

# def wall() :
#      brick= Turtle("square")
#      brick.color("blue")
#      brick.width(10)
#      brick.penup()
#      brick.setposition(290,-290)
#      brick.pendown()
#      brick.setposition(290,290)
#      brick.setposition(-290,290)
#      brick.setposition(-290,-290)
#      brick.setposition(290,-290)

# wall()

def up_wall() :
     brick= Turtle("square")
     brick.color("pink")
     brick.hideturtle()
     brick.width(5)
     brick.penup()
     brick.setposition(-295,270)
     brick.pendown()
     brick.setposition(295,270)
     brick.setposition(290,270)
     brick.setposition(290,-290)
     brick.setposition(-295,-290)
     brick.setposition(-295,270)


up_wall()
     
food = Food()
game_is_on= True
score = Score()
screen.onkey(key = "Up",fun = my_snake.move_up)
screen.onkey(key="Down",fun = my_snake.move_down)
screen.onkey(key = "Left",fun = my_snake.move_left)
screen.onkey(key="Right",fun = my_snake.move_right)
screen.onkey(key="i",fun = my_snake.increase_snake)
while game_is_on :
     screen.update()
     if score.score<=3 :
          my_time = 0.15
     elif score.score<=15 :
          my_time = 0.1
     elif score.score<=20 :
          my_time = 0.075
     else :
          my_time =0.05
     
     time.sleep(my_time)
     my_snake.move()
  
     
     if my_snake.segments[0].distance(food)<15:
          food.refresh()
          score.increase()
          my_snake.increase_snake()
      
     x_cor = my_snake.segments[0].xcor()
     y_cor = my_snake.segments[0].ycor()

     if x_cor > 290 or x_cor <-290 or y_cor > 270 or y_cor < -290 : 
          #ascreen.update()
          score.game_over()
          game_is_on = False
    
     for segment in my_snake.segments :
          if segment == my_snake.segments[0]:
               pass
          elif my_snake.segments[0].distance(segment) < 10:
               score.game_over()
               game_is_on = False

          
screen.exitonclick()