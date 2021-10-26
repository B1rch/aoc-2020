import itertools as it
import more_itertools as mi
import numpy as np
import fileinput, sys
from collections import defaultdict

sys.setrecursionlimit(10**6) #lol

def solve(line: str):
  buf = []
  for c in line:
    if buf and buf[-1] == c.swapcase():
      buf.pop()
    else:
      buf.append(c)
  return len(buf)
def part1(s: str):
  return solve(s)

def part2(s: str):
  letters = set([_s for _s in s.lower()])
  return min([solve(subS) for subS in [s.replace(l, '').replace(l.upper(), '') for l in letters]])


_s = fileinput.input().readline().strip()
part_1 = part1(_s)
print(f"\n----    PART 1    ----\n")
print(f'PART 1: {part_1}')
print(f"\n----------------------\n")

part_2 = part2(_s)
print(f"\n----    PART 2    ----\n")
print(f'PART 2: {part_2}')
print(f"\n----------------------\n")
