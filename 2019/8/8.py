from shared.helpers import print_decorator, time_decorator
import fileinput, os
import numpy as np

def parseData(fi):
  d = [line.strip() for line in fi.input()]
  size = tuple(map(int, d[0].split(','))) #rows, cols
  layers = int(len(d[1]) / np.prod(size))
  pixels = np.reshape([int(p) for p in d[1]], (layers, *size))
  return size, pixels


@time_decorator
@print_decorator
def part_1(pixels):
  bestLayer, checksum = 0, 0
  for layer in pixels:
    if (c:=np.count_nonzero(layer)) > bestLayer:
      bestLayer = c
      checksum = (layer == 1).sum() * (layer == 2).sum()
  return checksum

@time_decorator
@print_decorator
def part_2(pixels, size):
  out = np.full(size, " ", str)
  # 0 is black, 1 is white, and 2 is transparent.
  for cols in range(size[0]):
    for rows in range(size[1]):
      for p in pixels[:,cols,rows]:
        if p != 2:
          out[cols, rows] = '·' if p else '#'
          break
  return out

size, pixels = parseData(fileinput)
p1 = part_1(pixels)
print(f"checksum = {p1}")

def print2d(ar):
  return '\n'.join([' '.join(s) for s in ar])
p2 = part_2(pixels, size)
f = open('./out.txt', 'w')
f.write(print2d(p2))
f.close()
print(f"message found in out.txt")

