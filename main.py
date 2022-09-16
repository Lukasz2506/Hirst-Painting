#100 Days of Code, Angela Yu
# Day 18, Hirst Painting Project
#Student: Łukasz Świątek Brzeziński

#Aim: Paint one of the Hirst painting using Turtle module

from turtle import Turtle, Screen, colormode
from random import randint
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('dots.jpg', 30)
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)

#or simpler way to get the list:
# for color in colors:
#     r = color.rgb
#     rgb_colors.append(r)
#
# print(rgb_colors)


#now you can copy from terminal the list of colours, check on the rgb color browser which
# belongs to a background and delete that colors

colormode(255)

colour_list = [(157, 15, 23), (117, 167, 188), (30, 110, 158), (234, 83, 44),
               (124, 175, 145), (7, 98, 38), (172, 20, 15), (30, 130, 48),
               (182, 185, 27), (200, 63, 27), (11, 42, 76), (16, 62, 41),
               (238, 202, 8), (136, 83, 96), (91, 15, 25), (49, 166, 77),
               (37, 27, 23), (176, 135, 148), (6, 66, 137), (50, 151, 196),
               (215, 67, 72), (232, 169, 161), (167, 208, 174), (78, 133, 185)]

current_color = colour_list[randint(0,len(colour_list)-1)]
size = 20
distance_h = 50
distance_v = -200
dots_number = 10
draw = Turtle()

draw.hideturtle()
draw.penup()
for verse in range(0,10):
    draw.setx(-200)
    draw.sety(distance_v)
    for turn in range (10):
        draw.pendown()
        current_color = colour_list[randint(0,len(colour_list)-1)]
        draw.dot(size, current_color)
        draw.penup()
        draw.forward(distance_h)

    distance_v += 50


screen = Screen()
screen.exitonclick()