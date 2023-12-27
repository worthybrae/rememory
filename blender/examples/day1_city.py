import bpy
import random
import time
from mathutils import Vector


materials = [
    bpy.data.materials[1],
    bpy.data.materials[1],
    bpy.data.materials[1],
    bpy.data.materials[1],
    bpy.data.materials[2],
    bpy.data.materials[2],
    bpy.data.materials[0],
    bpy.data.materials[3]
]
sizes = [
    1,
    2, 
    4
]
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), size=1.0)
ob = bpy.context.object
ob.rotation_mode = 'XYZ'
obs = []
sce = bpy.context.scene

def index_exists(ls, i):
    return (0 <= i < len(ls)) or (-len(ls) <= i < 0)

def isFree(grid, x, y, width, height):
    for i in range(0, width, 1):
        for j in range(0, height, 1):
            if index_exists(grid, x + i) == False or index_exists(grid[x + i], y + j) == False or grid[x + i][y + j] != 0:
                return False
    return True

def setGridCube(grid, x, y, width, height, cubeIndex):
    for i in range(0, width, 1):
        for j in range(0, height, 1):
            grid[x + i][y + j] = cubeIndex
            
def placeCube(grid, count, width, height):
    for i in range(0, count, 1):
        for j in range(0, count, 1):
            if isFree(grid, i, j, width, height):
                return [i, j]
    return False

def rnd(scale):
    return (random.random() - 0.5) * scale * 2.0

def add_cube(x, z, width, height):
    y = 0
    yscale = random.randint(1, 2)
    if random.random() < 0.04:
        yscale = random.randint(3, 6)
    if random.random() < 0.004:
        yscale = random.randint(10, 50)
    for i in range(0, yscale, 1):
        current = ob.copy()
        current.location += Vector((x + width / 2 - 50, z + height / 2 - 50, y))
        current.scale = Vector((width, height, 1.0))
        rx = rnd(.1)
        ry = rnd(.1)
        rz = rnd(.1)
        current_rotation_euler = (rx, ry, rz)
        current.name = 'Cube({0}, {1})'.format(x, z)
        current.data.name = 'Mesh({0}, {1})'.format(x, z)
        mat = random.choice(materials)
        current.data = current.data.copy()
        current.data.materials.append(mat)
        y += 1
        x += rnd(0.1)
        z += rnd(0.1)
        bpy.context.collection.objects.link(current)
        
def make_cube(centerx = 0.0, centery = 0.0, centerz = 0.0):
    count = 200
    grid = []
    cubes = []
    cubeindex = 0
    for i in range(0, count, 1):
        grid.append([])
        for j in range(0, count, 1):
            grid[i].append(0)
    for k in range(0, count * count, 1):
        width = random.choice(sizes)
        height = random.choice(sizes)
        position = placeCube(grid, count, width, height)
        if position:
            setGridCube(grid, position[0], position[1], width, height, cubeindex)
            cubes.append(position)
            add_cube(position[0], position[1], width, height)
            cubeindex += 1

make_cube()
sce.update()