#!python3

from models.generators.map import Map
from models.generators.maze import Maze

map = Map(20, 40)
map.draw()
maze = Maze(map)
maze.generate()

