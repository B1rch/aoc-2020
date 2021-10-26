import fileinput, math
from shared.vector import Vector
import numpy as np

directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
def findInLine(bounds, curr: tuple[int, int], target: tuple[int, int], candidates: set[tuple[int, int]]):
  inline = set([target])
  vC, vT = Vector(*curr), Vector(*target)
  runRise = (vT - vC)
  slope = runRise // math.gcd(*runRise) # start at smallest form slope
  newTarget = vC + slope
  while 0 <= newTarget[0] <= bounds[0] and 0 <= newTarget[1] <= bounds[1]:
    if tuple(newTarget) in candidates:
      inline.add(tuple(newTarget))
    newTarget += slope
  return inline

def parseData():
  data = np.array([list(line.strip()) for line in fileinput.input()])
  S = set()

  for c in np.ndenumerate(data):
    if c[1] == '#': S.add(c[0])
  return data.shape, S

def part1(bounds, S: set[tuple[int,int]]):
  best, bestC = 0, None
  for curr in S:
    candidates = S.copy()
    candidates.remove(curr)
    total = 0
    while candidates:
      target = candidates.pop()
      total += 1
      candidates -= findInLine(bounds, curr, target, candidates)
      if total > best:
        best = total
        bestC = curr
  print(best, bestC)

part1(*parseData())
