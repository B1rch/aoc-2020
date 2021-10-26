import fileinput
import numpy as np
from math import prod

data = [list(map(int, line.strip().split('x'))) for line in fileinput.input()]

def calcValues(dims: list[int]) -> int:
  areas = [dims[0]*dims[1],dims[1]*dims[2],dims[2]*dims[0]]
  area = min(areas) + sum([2*a for a in areas])
  ribbon = sum(sorted(dims)[:2]) * 2 + prod(dims)
  return [area, ribbon]

totalArea, totalRibbon = list(map(sum, np.transpose([calcValues(line) for line in data])))
print(f"Total area needed = {totalArea}")
print(f"Total ribbon needed = {totalRibbon}")
