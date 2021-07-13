from ursina import *

class Voxel(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            position = (0,0,0),
            model = 'cube',
            origin_y = 0.5,
            texture ='white_cube',
            color = color.white,
            highlight_color = color.lime
        )

app = Ursina()


app.run()