from Tile import Tile

class Grid:
    def __init__(self, dimension):
        self.tiles = []
        self.dimension = dimension

    def fill_with_random_tiles(self):
        self.tiles = []
        for i in range(0, self.dimension):
            row = []
            for j in range (0, self.dimension):
                tile = Tile (i, j, False, False, False, False, 0)
                tile.init_randomly()

                row.append(tile)
            self.tiles.append(row)

    def find_connection(self, tile):
        i = tile.row
        j = tile.col
        self.used_tiles.append(tile)
        neighbours_list = []
        if tile.row - 1 >= 0:
            if tile.is_connected(self.tiles[tile.row - 1][j]):
                neighbours_list.append(self.tiles[tile.row - 1][j])
        if tile.row + 1 < self.dimension:
            if tile.is_connected(self.tiles[tile.row + 1][j]):
                neighbours_list.append(self.tiles[tile.row + 1][j])
        if tile.col - 1 >= 0:
            if tile.is_connected(self.tiles[i][j - 1]):
                neighbours_list.append(self.tiles[i][j - 1])
        if tile.col + 1 < self.dimension:
            if tile.is_connected(self.tiles[i][j + 1]):
                neighbours_list.append(self.tiles[i][j + 1])
        for k in neighbours_list:
            if k not in self.used_tiles:
                self.other_tiles_list.append(k)
                self.find_connection(k)

        return self.other_tiles_list

    def on_click(self, i, j):
        self.used_tiles = []
        self.other_tiles_list = []
        o_t_list = self.find_connection(self.tiles[i][j])
        self.tiles[i][j].rotate(1)
        for k in o_t_list:
            k.rotate(1)








