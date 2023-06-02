# ###This code will not work in repl.it as there is no access to the colorgram package here.###
# ##We talk about this in the video tutorials##
# import colorgram
# rgb_colors = []
# rgb_tuples = []
# colors = colorgram.extract('/Users/jamessingzon/Desktop/100DaysPython/Day_18/image.jpg', 30)
# for _ in range(len(colors)):
#     r = colors[_].rgb[0]
#     g = colors[_].rgb[1]
#     b = colors[_].rgb[2]
#     rgb_tuples.append((r,g,b))
# print(rgb_tuples)



# # for color in colors:
# #     rgb_colors.append(color.rgb)

# # print(rgb_colors)

import turtle as t
import random

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

screen = t.Screen()
t.colormode(255)
t.shape("turtle")
t.speed("fastest")
t.pu()

#Draw dots across
def dots_across():
    for _ in range(10):
        t.pd()
        t.color(random.choice(color_list))
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.pu()
        t.forward(70)

#Starting coordinates
x = -(screen.screensize()[0]) + screen.screensize()[0]//10
y = -(screen.screensize()[0]) + screen.screensize()[0]//10 + 35
def grid_start(start_x, start_y):
    t.pu()
    t.setpos(start_x, start_y)

#Move up a row
# def moving_up(repo_x,inc_y):
#     inc_y += 70
#     t.setpos(repo_x, inc_y)
#     return inc_y


grid_start(x,y)
for _ in range(10):
    dots_across()
    y += 70
    t.setpos(x, y)
t.hideturtle()


screen.exitonclick()