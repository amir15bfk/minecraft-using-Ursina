from ursina import *
from first_person_controller import FirstPersonController
import sys

app = Ursina()
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture  = load_texture('assets/dirt_block.png')
def update():
    if held_keys['k']:
        mouse.locked = False
    if held_keys['l']:
        mouse.locked = True
    if held_keys['r']:
        player.y+=10*time.dt
    if held_keys['f']:
        player.y-=10*time.dt

class Voxel(Button):
    def __init__(self,position=(0,0,0),texture= grass_texture ):
        super().__init__(
            parent = scene,
            position = position,
            model = 'assets/block',
            origin_y = 0.5,
            texture =texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.lime,
            scale = 0.5
        )
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                voxel =  Voxel(position = self.position + mouse.normal)
            if key == 'right mouse down':
                destroy(self)
            

for z in range(-8,8):
    for x in range(-8,8):
        voxel = Voxel((x,-2,z))
player = FirstPersonController()

app.run()