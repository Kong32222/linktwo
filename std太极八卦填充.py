from turtle import *
pensize(2)
import time
fillcolor('Black')
begin_fill()
circle(100, 180, steps=48)
circle(50, 180)
circle(-50, 180)
end_fill()

circle(-100, 180, steps=48)

up()
right(90)
fd(50)
seth(0)  #设置方向  并且是固定方向 不是第一次seth 90  再 seth 90  就是180 ；结果还是90;   
fd(25)
seth(90)
down()
fillcolor('White')
begin_fill()
circle(20, steps=24)  # 这是把圆分成24个小线段来近似画出一个圆。
end_fill()

up()
home()
seth(90)
fd(50)
left(90)
fd(25)
left(90)
down()
fillcolor('Black')
begin_fill()
circle(20, steps=24)
end_fill()
ht()