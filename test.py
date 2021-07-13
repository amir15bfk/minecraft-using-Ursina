from ursina import *

class Test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = 'cube',
            color = color.white,
            texture = 'white_cube',
            rotation = Vec3(45,45,45)
        )

def update():
    if held_keys['z']:
        test_square.z+=10*time.dt
    if held_keys['s']:
        test_square.z-=10*time.dt
    if held_keys['d']:
        test_square.x+=10*time.dt
    if held_keys['q']:
        test_square.x-=10*time.dt
    if held_keys['i']:
        test_cube.z+=10*time.dt
    if held_keys['k']:
        test_cube.z-=10*time.dt
    if held_keys['l']:
        test_cube.x+=10*time.dt
    if held_keys['j']:
        test_cube.x-=10*time.dt
class button(Button):
    def __init__(self):
        super().__init__(
            parent = scene,
            model='cube',
            texture = 'brick',
            color = color.blue,
            highlight_color = color.red,
            pressed_color = color.green
        )
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                print('Yessss ')


app = Ursina()
sans_texture = load_texture('assets/python.png')
test_square = Entity(model='cube',scale=(5,5,5),position=(0,-4,0),texture=sans_texture)

sans = Entity(model="quad",texture=sans_texture)

test_cube =button()
app.run()