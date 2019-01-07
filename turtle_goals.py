# exit imported to be able to exit main game loop.
# border is a module from seperate python file that sets borders for turtles
# turtle is the graphics module used for game.
# random used to get random place for turtles.
# math used in Collision class to get the distnce between the goal and player. 
from sys import exit
import border
import turtle
import random
import math

# sets characteristics of first screen
screen = turtle.Screen()
screen.bgcolor("pink")
screen.title("Playing around with the 'turtle' method.")

# class for the player's turtle
class Player(turtle.Turtle):

    # attributes of Player
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.color("white")
        self.speed = 1

    # next five methods set movement patterns of player's turtle
    def move(self):
        self.forward(self.speed)

        # how player turtle reacts to border
        if self.xcor() > 240 or self.xcor() < -240:
            self.right(70)
        if self.ycor() > 240 or self.ycor() < -240:
            self.right(70)

    def turn_left(self):
        self.left(40)

    def turn_right(self):
        self.right(40)

    def speed_increase(self):
        self.speed += 1

    def speed_decrease(self):
        self.speed -= 1

# trial is assigned to an instance of class Player(). 
trial = Player()

# keyboard bindings
turtle.listen()
turtle.onkey(trial.turn_left, "Left")
turtle.onkey(trial.turn_right, "Right")
turtle.onkey(trial.speed_increase, "Up")
turtle.onkey(trial.speed_decrease, "Down")

# class for goals that the player tries to catch
class Goal(turtle.Turtle):

    # attributes of Goal
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.color("green")
        self.shape("square")
        self.speed = 3
        self.goto(random.randint(-240, 240), random.randint(-240, 240))
        self.setheading(random.randint(0, 360))

    # how the goals move
    def move(self):
        self.forward(self.speed)

        # goals' reactions to the border
        if self.xcor() > 240 or self.xcor() < -240:
            self.right(70)
        if self.ycor() > 240 or self.ycor() < -240:
            self.right(70)

    # causes goals to "disappear"
    def disappear(self):
        self.goto(-1000, 1000)

# goals_list appended in later code to include more instances
# of Goal().
goals_list = [Goal()]


# returns true or false if player and goal collide
def Collision(player, goal):

    y = player.xcor() - goal.xcor()
    z = player.ycor() - goal.ycor()
    distance = math.sqrt((y**2) + (z**2))
    
    if distance < 20:
        return True
    else:
        return False

# Score class keeps track of and changes score
class Score(turtle.Turtle):

    # Score() attributes
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.score = 0

    # score wil change by one point
    def change_score(self, points):
        self.score += points

# score_count is assigned to an instance of class Score(). 
score_count = Score()

# FirstRoom comes after intial "room"; has two goals 
class FirstRoom(object):

    def blue_room(self):
        screen = turtle.bgcolor('blue')
        print("First Room Ran")

        for goal in range(0, 2):
            goals_list.append(Goal())
            print("goals_list is now", goals_list)
            print(f"gols now has {len(goals_list)} items")

# SecondRoom comes after FirstRoom; has three goals
class SecondRoom(object):

    def yellow_room(self):
        screen = turtle.bgcolor('yellow')
        print("second Room Ran")

        for goal in range(0, 3):
            goals_list.append(Goal())
            print("goals_list is now", goals_list)
            print(f"gols now has {len(goals_list)} items")

# ThirdRoom comes after SecondRoom; has four goals
class ThirdRoom(object):
    
    def purple_room(self):
        screen = turtle.bgcolor('purple')
        print("third Room Ran")

        for goal in range(0, 4):
            goals_list.append(Goal())
            print("goals_list is now", goals_list)
            print(f"gols now has {len(goals_list)} items")

# for smoother graphics
screen.tracer(0)

# the main game loop
class MainLoop(object):

    def main_loop(self):

        while True:
            screen.update()
            # player moves
            trial.move()
            # each goal will move
            for each_goal in goals_list:
                each_goal.move()
                # collision with goal causes score change
                if Collision(trial, each_goal):
                    print("Collision just ran")
                    each_goal.disappear()
                    score_count.change_score(1)

            # Moves screen to FirstRoom class and methods. 
            if score_count.score == 1:
                score_count.score = 10
                print("score_count.score is now", score_count.score)
                print("if statement ran")
                next_room = FirstRoom()
                next_room.blue_room()

            # Moves screen to SecondRoom class and methods. 
            if score_count.score == 12:
                score_count.score = 20
                print("score_count.score is now", score_count.score)
                print("next if statement ran")
                next_room = SecondRoom()
                next_room.yellow_room()

            # Moves screen to ThirdRoom class and methods. 
            if score_count.score == 23:
                score_count.score = 30
                print("score_count.score is now", score_count.score)
                print("next if statement ran")
                next_room = ThirdRoom()
                next_room.purple_room()
                
            # Exits the main loop. 
            if score_count.score == 34:
                exit(0)


# game_1 instance of MainLoop()
game_1 = MainLoop()
game_1.main_loop()