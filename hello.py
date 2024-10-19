from turtle  import *
import time 
'''
控制画笔在画布上前进、后退、向左转或向右转,画出H字形的痕迹

'''
pensize(5)        # 控制 笔的大小
pencolor("red")   # 控制 笔的颜色
ht()              # 隐藏 箭头
angle = 60
distance_ = 100

left(angle)
fd(distance_)

home()  #  
 
fd(distance_)
 
left(90 + 30)

fd(distance_)
 

clear()
up()
home()  #回到 原点 也是笔还在画画 ，所以得up起来， 到了指定的地方再down（）
down()
circle(50, 180)

 

time.sleep(1)