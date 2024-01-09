#Author: Minh Nguyen
#Date: 10/04/2023
#Purpose: CS1 - Write a program opens up a graphics window
#and allows user to use the mouse to draw on a simulated chalkboard.

from cs1lib import *

#global variables
#old_x and old_y store the end point of most recent line that was drawn in main draw function.
old_x = 0
old_y = 0
#curr_x and curr_y store the current location of the mouse.
curr_x = 0
curr_y = 0
mpressed = False #default mousepressed
draw_background = True

def draw_points(x1, y1, x2, y2): #draw a pixel any time the mouse is pressed down.
    enable_stroke()
    set_stroke_width(2)
    draw_line(x1, y1, x2, y2)

def main_draw(): #main draw function
    global old_x, old_y, curr_x, curr_y, draw_background, mpressed
    #set initial background black and default stroke color white.
    if draw_background == True:
        set_clear_color(0, 0, 0)
        clear()
        set_stroke_color(1, 1, 1)
        draw_background = False

    if mpressed == True: #draw a line between the points (old_x, old_y) and (curr_x, curr_y),
        #update old_x and old_y to remember the end point of the last line drawn.
        draw_points(old_x, old_y, curr_x, curr_y)
        old_x = curr_x
        old_y = curr_y

def mmove(mx, my): #update the value of curr_x and curr_y.
    global curr_x, curr_y
    if mpressed == True:
        curr_x = mx
        curr_y = my

def mpress(mx, my): #If the mouse button is pressed down,
    #the board is drawn on using the current chalk color.
    global old_x, old_y, curr_x, curr_y, mpressed
    old_x = mx
    old_y = my
    curr_x = mx
    curr_y = my
    mpressed = True

def mrelease(mx, my): #If the mouse button is released,
    #the user should be able to move the mouse pointer around without drawing anything.
    global mpressed
    mpressed = False

def kpress(value): #capability to draw colors.
    if value == "r": #red
        set_stroke_color(1, 0, 0)
    if value == "g": #green
        set_stroke_color(0.2, 1, 0)
    if value == "b": #blue
        set_stroke_color(0, 1, 1)
    if value == "y": #yellow
        set_stroke_color(1, 0.8, 0)
    if value == "p": #pink
        set_stroke_color(1, 0, 1)

start_graphics(main_draw, mouse_press=mpress, mouse_move=mmove, mouse_release=mrelease, key_press=kpress)