from turtle import Turtle,Screen
SNAKE_COLOR = "green"
SNAKE_SHAPE ="circle"
class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
             segment = Turtle(SNAKE_SHAPE)
             segment.color(SNAKE_COLOR)
             segment.up()
             segment.setpos(-i*20,0)
             segment.speed("fastest")
             self.segments.append(segment)
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x= self.segments[i-1].xcor()
            new_y= self.segments[i-1].ycor()
            self.segments[i].setpos(new_x,new_y)
        self.segments[0].forward(20)

    def move_left(self):
        angle = self.segments[0].heading()
        for i in range(len(self.segments)-1,0,-1):
            new_x= self.segments[i-1].xcor()
            new_y= self.segments[i-1].ycor()
            self.segments[i].setpos(new_x,new_y)
        if angle == 90:
            self.segments[0].left(90)
        elif angle == 270:
            self.segments[0].right(90)
        else:
            self.segments[0].forward(20)

    def move_up(self):
        angle = self.segments[0].heading()
        for i in range(len(self.segments)-1,0,-1):
            new_x= self.segments[i-1].xcor()
            new_y= self.segments[i-1].ycor()
            self.segments[i].setpos(new_x,new_y)

        if angle==0 :
            self.segments[0].left(90)
        elif angle==180 :
            self.segments[0].right(90)
        else:
            self.segments[0].forward(20)

    def move_down(self):
        angle = self.segments[0].heading()
        for i in range(len(self.segments)-1,0,-1):
            new_x= self.segments[i-1].xcor()
            new_y= self.segments[i-1].ycor()
            self.segments[i].setpos(new_x,new_y)

        if angle==0 :
            self.segments[0].right(90)
        elif angle==180 :
            self.segments[0].left(90)
        else:
            self.segments[0].forward(20)

    def move_right(self):
        angle = self.segments[0].heading()
        for i in range(len(self.segments)-1,0,-1):
            new_x= self.segments[i-1].xcor()
            new_y= self.segments[i-1].ycor()
            self.segments[i].setpos(new_x,new_y)
    
        if angle==90 :
            self.segments[0].right(90)
        elif angle==270 :
            self.segments[0].left(90)
        else:
            self.segments[0].forward(20)
        

    def increase_snake(self):
        segment = Turtle(SNAKE_SHAPE)
        segment.color(SNAKE_COLOR)
        segment.up()
        segment.speed("fastest")
        new_x = self.segments[len(self.segments)-1].xcor()
        new_y = self.segments[len(self.segments)-1].ycor()
        segment.setpos(new_x,new_y)
        segment.backward(20)
        self.segments.append(segment)
        


            