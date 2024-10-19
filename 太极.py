 
import time
from turtle import *

def draw_yin_yang(radius):
    # 设置背景颜色为白色
    bgcolor("white")  
    
    # 画出外圈
    penup()
    goto(0, -radius)
    pendown()
    circle(radius)
    
    # 画左边的黑色半圆
    penup()
    goto(0, 0)
    # setheading(180)  # 朝向左边
    pendown()
    color("black")
    begin_fill()
    goto(0, -radius)
    circle(radius, 180)  # 逆时针画半圆
    goto(0, 0)
    end_fill()
    

    up()
    goto(0,0)
    down()
    pencolor("black")
    begin_fill()
    circle(radius/2 , 180)
    end_fill()

    up()
    goto(0,radius)
    down()
    begin_fill()
    color("white")
    circle(-radius/2 , 180)
    end_fill()

    # 画出外圈
    penup()
    color("black")
    goto(0, radius)
    pendown()
    circle(radius)

    # 画右边的白色半圆
    size = 25
    local_X = 15
    penup()
    goto(local_X , radius/2)
    # setheading(0)  # 朝向右边
    pendown()
    color("black")
    begin_fill()
    # circle(radius/8)   
    dot(size, "black")
    end_fill()
    
    # 画左边的小白圆（在黑色区域内）
    penup()
    goto(-local_X, -(radius /2))  # 移动到左半部分)
    pendown()
    color("white")
    begin_fill()
    dot(size ,"white")
    end_fill()
 
    

# 设置乌龟的速度和隐藏
speed(3)
hideturtle()
# 绘制左右对称的太极八卦图，半径为100
draw_yin_yang(100)

# 完成绘图
done()


time.sleep(1)
