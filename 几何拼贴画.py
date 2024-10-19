from turtle  import *
import time

pensize(50);pencolor("lightgreen")
ht()

# 大地
up()
goto(-400, -200)
down()
goto(400, -200)


# 栏杆
pensize(20);pencolor("goldenrod")
up();goto(-400, -150);down();goto(400,-150)# ------
up();goto(-250, -200);down();goto(-250,-100)#  |
up();goto(-100, -200);down();goto(-100,-100)#  |
up();goto(30, -200);down();goto(30,-100)    #  |
up();goto(300,  -200);down();goto(300,-100) #  |


# 树干
pensize(30);pencolor("Olive")
up(); goto(-150, -200);down(); goto(-150, -120)

#树冠
pensize(1);pencolor("green")
up();goto(-80, -120);down()
begin_fill();seth(60);circle(80,steps=3);end_fill()

up();goto(-95, -50);down()
begin_fill();seth(60);circle(60,steps=3);end_fill()
up();goto(-115, 0);down()  # 原来是100  ；我修改成了115 感觉最上面的三角比较合适
begin_fill();seth(60);circle(40,steps=3);end_fill()

# 画房子。房子可分解为墙体、房顶、窗户、门和烟囱等 
pensize (1) ;color ('RoyalBlue' )
up();home();fd(70);right(90) ;down()
begin_fill();fd(200); left(90) ;fd(200);left(90) ;fd(200);end_fill()

#烟囱,画一条长为 90像素的线段,画笔大小 30像素,填充颜色'DimGray
pensize (30) ;pencolor ('DimGray')
up();goto (230,30);down();goto(230, 120)  #两点之间的距离：就是Y 轴； 


#房顶,画一个底角为 30度、腰为 200像素的等腰三角形,填充颜色'DeepPink
pensize (1) ;color ('DeepPink' );up ();home();down ()
begin_fill();left (30);fd(200);right(60) ;fd (200) ;home ();end_fill ()
#窗户,画一个半径为 50像素的圆的内切正 4边形,填充颜色'violet
color('Violet');up();goto(160,-90);down (); 
begin_fill();seth(45);circle (50,steps= 4);end_fill ()

#门,画一个长 120像素、宽 60像素的长方形,填充颜色'chocolate'
color('chocolate');up();goto(250,-200);down ();seth (90)
begin_fill() 
fd(120) ;left (90);fd (60);left (90) ;fd(120) ;left (90) ;fd (60)
end_fill()

#炊烟,画3个依次变小的圆点, 填充颜色 'aliceBlue'
up(); goto(250, 160);dot(30, "AliceBlue")
goto(270, 200); dot(20, 'AliceBlue')
goto(300, 220); dot(10,"AliceBlue")
#太阳,画一个 80像素的圆点, 填充颜色 'Gold'
goto(-260, 250); dot(80,'Gold')

time.sleep(1)
