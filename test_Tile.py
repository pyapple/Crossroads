from unittest import TestCase
from Tile import Tile

class TestTile(TestCase):
    def test_init(self):
        tile = Tile (2, 3, False, True, True, False, 0)  # row, col, top, right, bottom, left, rotation_angle

        self.assertEqual(tile.row, 2, "Row should be equal to 2")
        self.assertEqual(tile.col, 3, "Col should be equal to 3")

        self.assertFalse (tile.top)
        self.assertTrue (tile.right)
        self.assertTrue (tile.bottom)
        self.assertFalse (tile.left)

    def test_is_connected(self):
        tile1 = Tile (2, 3, False, True, True, False, 0)
        tile2 = Tile (1, 3, True, False, True, True, 0)
        tile3 = Tile (2, 4, False, True, True, True, 0)

        self.assertFalse(tile1.is_connected(tile2))
        self.assertFalse(tile2.is_connected(tile1))
        self.assertFalse(tile2.is_connected(tile3))
        self.assertFalse(tile1.is_connected(tile1), "tile shouldn't be considered connected to itself")

        self.assertTrue(tile1.is_connected(tile3))
        self.assertTrue(tile3.is_connected(tile1))



