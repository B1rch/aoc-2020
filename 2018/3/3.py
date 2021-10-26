import itertools as it
import more_itertools as mi
import numpy as np
import fileinput, math
from collections import defaultdict

def gridPrint(grid):
  for line in grid:
    s = " ".join([str(x) for x in line])
    print(f'{s}\n')


data = defaultdict(dict)
for line in fileinput.input():
  id,_,coords,size = str(line).strip().split(' ', maxsplit=3)
  id = id[1:]
  x,y = coords[:-1].split(',')
  w,h =  size.split('x')
  data[id] = tuple(map(int,(x,y,w,h)))


def doOverlap(a,b):
  # If one rectangle is on left side of other
  if(a[0] >= b[0] + b[2] or b[0] >= a[0] + a[2]):
      return False
  # If one rectangle is above other
  if(a[1] <= b[1] + b[3] or b[1] <= a[1] + a[3]):
      return False
  return True

def fillSheet():
  mw, mh = max([x+w for x,_,w,_ in data.values()]), max([y+h for _,y,_,h in data.values()])
  return np.zeros((mw,mh), dtype=int)

def part1(sheet):
  for x,y,w,h in data.values():
    sheet[y:y+h, x:x+w] += 1
  return sheet, np.count_nonzero(sheet > 1)
def part2(sheet):
  for id,(x,y,w,h) in list(data.items()):
    if all(sheet[y:y+h, x:x+w].flatten() == 1):
      return id
  return 'test'

sheet = fillSheet()
newSheet, part_1 = part1(sheet)
print(f"\n----    PART 1    ----\n")
print(f'PART 1: {part_1}')
print(f"\n----------------------\n")

part_2 = part2(newSheet)
print(f"\n----    PART 2    ----\n")
print(f'PART 2: {part_2}')
print(f"\n----------------------\n")
