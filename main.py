import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

#EXTRAXT RBG FROM ORIGINAL JPEG TO GET color_list
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('Hirst-Spots-1024x665.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(253, 251, 246), (244, 251, 247), (206, 159, 112), (252, 247, 249), (226, 237, 244), (138, 173, 192),
              (223, 206, 119), (43, 106, 138), (139, 183, 149), (15, 52, 75), (218, 88, 65), (36, 126, 105),
              (124, 81, 95), (193, 133, 145), (71, 164, 120), (145, 81, 71), (12, 58, 49), (55, 153, 180), (51, 34, 43),
              (126, 37, 50), (205, 85, 102), (175, 206, 171), (6, 109, 87), (229, 168, 182), (147, 204, 230),
              (157, 153, 67), (33, 64, 101), (16, 84, 100), (47, 30, 27), (184, 189, 203)]

#locate first dot
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range (1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
