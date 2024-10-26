import pyglet
img_path = "clown-fish.gif"

game_win = pyglet.window.Window(width=800, height=600)
try:

    img = pyglet.resource.animation(img_path)
 
except pyglet.resource.ResourceNotFoundException:
    print("Image not found")
    exit()

fish = pyglet.sprite.Sprite(img, x = 400, y= 200)    # 小精灵；电脑子画面

#@ 符号后面是 game_win.event。这里，
# @ 符号在 Python 中用作装饰器（decorator）的语法。
# 装饰器是一种允许用户在不修改原有函数或方法定义的情况下，给函数或方法添加额外功能的高级功能。
@game_win.event
def on_draw():
    game_win.clear()
    fish.draw()

pyglet.app.run()