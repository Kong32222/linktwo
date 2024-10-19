from turtle  import *
import time 
'''
控制画笔在画布上前进、后退、向左转或向右转,画出H字形的痕迹

'''
pensize(5)        # 控制 笔的大小
pencolor("red")   # 控制 笔的颜色
# ht()              # 隐藏 箭头
fd(100)
seth(90)
fd(100)
seth(180)
fd(100)

# circle(50, 180)      # 半径是 50px
# circle(-50, steps=3) # steps 参数为3, 将会在一个半径为 50 像素的圆内画个内切正三边形(等边三角形) 
# dot(20, "green")
time.sleep(1)
