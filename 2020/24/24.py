from collections import defaultdict
import fileinput, re
from typing import Generator, Tuple

__AXIAL_DIRECTIONS = [
  (+1, 0), (+1, -1), (0, -1),
  (-1, 0), (-1, +1), (0, +1),
]

def neighbours(coords):
  return [(coords[0] + c[0], coords[1] + c[1]) for c in __AXIAL_DIRECTIONS]

def doStep(grid: set):
  cpy = grid.copy()
  for coords in grid:
    nbs = neighbours(coords)
    blackNeighbours = [nb for nb in nbs if nb in grid]
    if len(blackNeighbours) == 0 or len(blackNeighbours) > 2:
      cpy.remove(coords)
    for nb in nbs:
      if len([_nb for _nb in neighbours(nb) if _nb in grid]) == 2:
        cpy.add(nb)
  return cpy


dirRe = re.compile('(e|se|sw|w|nw|ne)')
data = [line.strip() for line in fileinput.input()]
flipped = defaultdict(int)
dirMap = {
  'e':  ( 1 ,  0),
  'se': ( 0 ,  1),
  'sw': (-1 ,  1),
  'w':  (-1 ,  0),
  'nw': ( 0 , -1),
  'ne': ( 1 , -1),
}

for line in data:
  match = re.findall(dirRe, line)
  coords = tuple(map(sum, zip(*[dirMap[dir] for dir in match])))
  flipped[coords] += 1

onlyBlackTiles = {k:v for k,v in flipped.items() if v % 2 == 1}
print(f'PART_1 : {len(onlyBlackTiles)}')

grid = set([k for k in onlyBlackTiles.keys()])

for _ in range(100):
  grid = doStep(grid)
print(f'PART_2 : {len(grid)}')
