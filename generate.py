#!python3

import argparse
import random
from models.logger import Logger
from models.rect import Rect
from models.coordinate import Coordinate
from models.node import Node
from models.dungeon_generator import DungeonGenerator

description = "Pass columns, rows, and filename for map"
parser = argparse.ArgumentParser(description=description)
parser.add_argument("-c", "--columns", help="number of columns for map", type=int)
parser.add_argument("-r", "--rows", help="number of rows for map", type=int)
parser.add_argument("-f", "--filename", help="name of file to save for map")
parsed_args = parser.parse_args()

generator = DungeonGenerator(parsed_args.rows, parsed_args.columns)
generator.draw()
