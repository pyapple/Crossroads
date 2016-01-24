import random
import numpy

from Constant import source, TILE_SIZE, TILE_CENTER, values_of_tiles

class Tile:
    def __init__(self, row, col, top, right, bottom, left, rotation_angle):

        self.row = row
        self.col = col
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.rotation_angle = 0


    def get_top(self):
        return self.top

    def get_right(self):
        return self.right

    def get_bottom(self):
        return self.bottom

    def get_left(self):
        return self.left

    def init_randomly(self):
        self.tile_code = random.choice(values_of_tiles)
        self.tile_code_changed = self.tile_code
        rotation_angle_coefficient = random.choice([0, 1, 2, 3])
        self.rotate(rotation_angle_coefficient)


    def is_connected(self, other_tile):
        if self.row == other_tile.row:
            if self.col == other_tile.col - 1:
                if self.get_right() == True and other_tile.get_left() == True:
                    return True
                else:
                    return False
            elif self.col == other_tile.col + 1:
                if self.get_left() == True and other_tile.get_right() == True:
                    return True
                else:
                    return False
        elif self.col == other_tile.col:
            if self.row == other_tile.row - 1:
                if self.get_bottom() == True and other_tile.get_top() == True:
                    return True
                else:
                    return False
            elif self.row == other_tile.row + 1:
                if self.get_top() == True and other_tile.get_bottom() == True:
                    return True
                else:
                    return False
        else:
            return False

    def rotate(self, rotation_angle_coefficient):

        tile_code_list_mod = list(self.tile_code_changed)
        tile_code_list = [0, 0, 0, 0]

        for i in range(0, len(tile_code_list_mod)):
            k = tile_code_list_mod[i]
            tile_code_list[(i + rotation_angle_coefficient) % 4] = k

        self.top = tile_code_list[0] == 'T'
        self.right = tile_code_list[1] == 'T'
        self.bottom = tile_code_list[2] == 'T'
        self.left = tile_code_list[3] == 'T'

        self.rotation_angle += (numpy.pi / 2) * rotation_angle_coefficient
        self.tile_code_changed = ''.join(tile_code_list)





