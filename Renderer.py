from Constant import source, TILE_SIZE, TILE_CENTER, values_of_tiles
import simpleguitk as simplegui


class Renderer:
    def __init__(self):
        self.images = []
        for i in range(1, 13):
            image = simplegui.load_image(source + str(i) + ".png")
            self.images.append(image)


    def render_grid(self, canvas, grid):
        new_tile_center = [0, 0]
        new_tile_center[0] = (TILE_CENTER[0] * 3) / grid.dimension
        new_tile_center[1] = (TILE_CENTER[1] * 3) / grid.dimension
        new_tile_size = [0, 0]
        new_tile_size[0] = (TILE_SIZE[0] * 3) / grid.dimension
        new_tile_size[1] = (TILE_SIZE[1] * 3) / grid.dimension
        for row in grid.tiles:
            for tile in row:
                tile_loc = [new_tile_center[0] + new_tile_size[0] * tile.col, new_tile_center[1] + new_tile_size[1] * tile.row]
                canvas.draw_image(self.image_for_tile(tile),  TILE_CENTER, TILE_SIZE, tile_loc, new_tile_size, tile.rotation_angle)


    def image_for_tile(self, tile):
        image_number = values_of_tiles.index(tile.tile_code)

        return self.images[image_number]
