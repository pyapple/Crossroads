import simpleguitk as simplegui

from Tile import Tile
from Grid import Grid
from Renderer import Renderer
from Constant import source, TILE_SIZE, TILE_CENTER, values_of_tiles

grid = Grid(3)
grid.fill_with_random_tiles()
renderer = Renderer()

def reset():
    global grid
    grid = Grid(grid.dimension)

    grid.fill_with_random_tiles()

def click(pos):
    j = pos[0] // int((TILE_SIZE[0] * 3) / grid.dimension)
    i = pos[1] // int((TILE_SIZE[1] * 3) / grid.dimension)
    grid.on_click(i, j)

def input_handler(text_input):
    grid.dimension = int(text_input)
    reset()

def draw_handler(canvas):
    renderer.render_grid(canvas, grid)

frame = simplegui.create_frame('Crossroads', TILE_SIZE[0] * 3, TILE_SIZE[1] * 3)
frame.set_mouseclick_handler(click)
frame.add_button("Reset", reset, 200)
frame.add_input('My label', input_handler, 50)

frame.set_draw_handler(draw_handler)

frame.start()
reset()
