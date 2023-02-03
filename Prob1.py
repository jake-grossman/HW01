#====================================================
# Filename: Prob1.py
# 
# Your name: Jake Grossman
# Who did you work with (if anyone)?:none
# Estimate for time spent (in hrs)?:1 hour
#====================================================

import karel

# Your program should create a checkerboard pattern on any
# rectangular world. I am defining a function below to
# get you started, but you can (and should) add whatever
# other helper functions you want below.

def create_checkerboard():
    """ Main function to create the checkerboard pattern. """
    # You need to add code here
    while left_is_clear() and front_is_clear():
        fill_row()
        if left_is_clear():
            next_line_right_side()
        if front_is_clear():
            fill_row()
        if right_is_clear():
            next_line_left_side()
        else:
            turn_left()
            turn_left()
    if front_is_blocked():
        turn_left()
        fill_row()
    if no_beepers_present() and front_is_clear():
        move()
        if no_beepers_present():
            turn_left()
            turn_left()
            move()
            turn_left()
            turn_left()
            fill_row()




def fill_row():
    #creates one row of every other space a beeper
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()
            if front_is_blocked():
                put_beeper()
            

def next_line_right_side():
    #move to the next line on the right side
    if no_beepers_present():
        turn_left()
        move()
        turn_left()
    else:
        turn_left()
        move()
        turn_left()
        move()

def next_line_left_side():
    #move to the next line on the left side
    if no_beepers_present():
        turn_right()
        move()
        turn_right()
    else:
        turn_right()
        move()
        turn_right()
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Remember to define any more helper functions you want down here


