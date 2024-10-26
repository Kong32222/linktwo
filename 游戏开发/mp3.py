import pyglet

sound1 = pyglet.resource.media('音乐珊瑚.mp3', streaming=False)
sound2 = pyglet.resource.media('music.mp3', streaming=False)

player = pyglet.media.Player()
player.play()