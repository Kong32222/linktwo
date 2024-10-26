import pyglet
game_win = pyglet.window.Window()

lable = pyglet.text.Label("hello world!",x= 100 ,y= 100)

@game_win.event
def  on_draw():
    game_win.clear()
    lable.draw()

pyglet.app.run()

    
