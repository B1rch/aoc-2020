from typing import Dict
import numpy as np
import fileinput, math, sys, time
from collections import defaultdict
# from itertools import chain, combinations

### END UTILS

def solve(amount: int, numList: list[int],lastSeen: dict[int]):
  #[0..2019]
  for _ in range(amount - (len(numList))):
    last = numList[-1]
    if (last not in lastSeen):
      numList.append(0)
    else:
      numList.append(len(numList) - lastSeen[last])
    lastSeen[last] = len(numList)-1
  return numList[-1]


numList = [int(n) for line in fileinput.input() for n in line.strip().split(',')]
lastSeen = defaultdict(int)
lastSeen |= {n:i+1 for i,n in enumerate(numList[:-1])} # all but last

part_1 = solve(2020,numList, lastSeen)
print(f"\n----    PART 1    ----\n")
print(f'PART 1: {part_1}')
print(f"\n----------------------\n")

s = time.perf_counter()
part_2 = solve(30000000, numList, lastSeen)
e = time.perf_counter()
print(f"\n----    PART 2    ----\n")
print(f'PART 2: {part_2} in in {(e - s):0.2f} s')
print(f"\n----------------------\n")
