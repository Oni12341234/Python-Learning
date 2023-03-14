import colorgram
import random
import turtle

# rgb_colors=[]
# colors = colorgram.extract('image.jpeg', 30)
# for color in colors:
    # r = color.rgb.r
    # g = color.rgb.g
    # b = color.rgb.b
    # new_color = (r, g, b)
    # rgb_colors.append(new_color)
# 
# 
# print(rgb_colors)
# 
color_list = [(249, 246, 240), (240, 250, 246), (251, 243, 249), (241, 245, 250), (35, 19, 15), (197, 144, 123), (30, 106, 155), (142, 85, 55), (9, 21, 45), (236, 213, 85), (196, 135, 155), (156, 62, 90), (221, 85, 66), (153, 17, 37), (202, 79, 104), (14, 54, 30), (162, 163, 35), (118, 172, 196), (41, 125, 79), (77, 12, 22), (120, 188, 160), (18, 92, 53), (11, 58, 137), (23, 201, 179), (23, 174, 206), (139, 222, 208), (149, 23, 16), (223, 172, 191), (233, 172, 162), (238, 206, 8)]
turtle.colormode(255)
oni = turtle.Turtle()
oni.width(5)
oni.hideturtle()
def draw_row():
    for i in range(10):
        oni.color(random.choice(color_list))
        oni.pendown()
        oni.dot()
        oni.penup()
        oni.forward(50)
        

for j in range(10):
    if j%2 == 0:
        draw_row()
    else:
        oni.right(90)
        oni.forward(50)
        oni.right(90)
        draw_row()
        oni.left(90)
        oni.forward(50)
        oni.left(90)
    
















screen = turtle.Screen()
screen.onclick()