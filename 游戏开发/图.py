import pyglet
img_path = "plan.png"

game_win = pyglet.window.Window(width=800, height=600)
try:
    # img = pyglet.image.load("")
    img = pyglet.resource.image(img_path)
    print(f"Image loaded: {img.width}x{img.height}")
except pyglet.resource.ResourceNotFoundException:
    print("Image not found")
    exit()

plan = pyglet.sprite.Sprite(img, x = 200, y= 200)

#@ 符号后面是 game_win.event。这里，
# @ 符号在 Python 中用作装饰器（decorator）的语法。
# 装饰器是一种允许用户在不修改原有函数或方法定义的情况下，给函数或方法添加额外功能的高级功能。
@game_win.event
def on_draw():
    game_win.clear()
    #img.blit(0, 0)
    plan.draw()

pyglet.app.run()