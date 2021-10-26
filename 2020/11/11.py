import numpy as np

def gridPrint(grid):
  for line in grid:
    str = " ".join(line)
    print(f'{str}\n')

def getNeighbours(grid, j ,i):
  adjecentIndices = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
  adjecents = []
  for y,x in adjecentIndices:
    if (j+y >= 0 and j+y < len(grid) and i+x >= 0 and i+x < len(grid[0])):
      adjecents.append(grid[j+y][i+x])
  return adjecents

def getVisibleSeats(grid, j ,i):
  directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
  visible = []
  for y,x in directions:
    _y, _x = y, x
    while (True):
      if (j+y < 0 or j+y >= len(grid) or i+x < 0 or i+x >= len(grid[0]) ):
        break
      if (grid[j+y][i+x] in ['#', 'L']):
        visible.append(grid[j+y][i+x])
        break
      y += _y; x+= _x
  return visible
data = np.loadtxt('11/data.txt', dtype=str)
# data = np.loadtxt('11/test.txt', dtype=str)

grid = [list(line) for line in data]

def doRoundPart1(grid):
  rows, cols, = len(grid), len(grid[0])
  tmp = np.array(grid).copy()
  for j in range(rows):
    for i in range(cols):
      adjecents = getNeighbours(grid, j, i)
      if (grid[j][i] == 'L'):
        if (np.all(np.array(adjecents) != '#')):
          tmp[j][i] = '#'
        #if all([x != '#' for x in adjecents]):
      elif(grid[j][i] == '#'):
        if (np.count_nonzero(np.array(adjecents) == '#') >= 4):
          tmp[j][i] = "L"
  return tmp

def doRoundPart2(grid):
  rows, cols, = len(grid), len(grid[0])
  tmp = np.array(grid).copy()
  for j in range(rows):
    for i in range(cols):
      visible = getVisibleSeats(grid, j, i)
      if (grid[j][i] == 'L'):
        if (np.all(np.array(visible) != '#')):
          tmp[j][i] = '#'
      elif(grid[j][i] == '#'):
        if (np.count_nonzero(np.array(visible) == '#') >= 5): # 5 here instead of 4
          tmp[j][i] = "L"
  return tmp

def part1():
  prev = doRoundPart1(grid)
  while (True):
    curr = doRoundPart1(prev)
    cmp = np.array(prev) == np.array(curr)
    if (cmp.all()):
      return curr
    prev = np.array(curr).copy()

def part2():
  prev = doRoundPart2(grid)
  while (True):
    curr = doRoundPart2(prev)
    cmp = np.array(prev) == np.array(curr)
    if (cmp.all()):
      return curr
    prev = np.array(curr).copy()

print('---PART ONE---\n\n')
out = part1()
gridPrint(out)
occ = np.count_nonzero(np.array(out) == '#')
print(f'\nOccupied seats: {occ}')
print('\n\n---PART ONE---')

print('---PART TWO---\n\n')
out = part2()
gridPrint(out)
occ = np.count_nonzero(np.array(out) == '#')
print(f'\nOccupied seats: {occ}')
print('\n\n---PART TWO---')
