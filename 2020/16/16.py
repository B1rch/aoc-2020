import numpy as np
import fileinput, math, sys, time
from collections import defaultdict

from numpy.lib.function_base import diff
# from itertools import chain, combinations



def part1(valids: dict[set[int]], others: list[list[int]]):
  validsList = [x for s in valids.values() for x in s]
  invalid, newOthers = [], [*others]
  for item in others:
    discard = False
    for n in item:
      if n not in validsList:
        invalid.append(n)
        discard = True
    if discard:
      newOthers.remove(item)
  return sum(invalid), newOthers


def part2(valids: dict[set[int]], others, myticket):
  others = np.array(others).transpose()
  columnTypes = np.zeros(others.shape[0], dtype=set)
  for i in range(others.shape[0]): columnTypes[i] = set()
  for i,line in enumerate(others):
    for t,s in valids.items():
      if all([x in s for x in line]):
         columnTypes[i].add(t)
  while not all([len(x)==1 for x in columnTypes]):
    seen = set()
    for s in columnTypes:
      if len(s) == 1: seen= seen.union(s)
    for i,s in enumerate(columnTypes):
      if (len(s)) > 1:
        columnTypes[i] = s.difference(seen)
  out = 1
  for i, t in enumerate(columnTypes):
    if list(t)[0].startswith('departure'):
      out *= myticket[i]
  return out

def parseInput():
  fi = fileinput.input()
  iNumbers, iMy, iNearby = [int(x) for x in fi.readline().strip().split(',')]
  valids, myTicket, others = defaultdict(set[int]), list[int], list[list[int]]
  lines = [line.strip() for line in fi]

  for line in lines[0:iMy]:
    if line =='': break
    t, ranges = line.split(': ')
    for r in ranges.split(' or '):
      l,r = r.split('-')
      for rr in range(int(l), int(r)+1): valids[t].add(rr)

  myTicket = [int(x) for x in lines[iMy].split(',')]
  others = [[int(x) for x in line.split(',')] for line in lines[iNearby:]]
  return valids, myTicket, others

valids, myTicket, others = parseInput()

s = time.perf_counter()
part_1, newOthers = part1(valids, others)
e = time.perf_counter()
print(f"\n----    PART 1    ----\n")
print(f'PART 1: {part_1} in {(e - s)*1000:0.3f} ms')
print(f"\n----------------------\n")

s = time.perf_counter()
part_2 = part2(valids, newOthers, myTicket)
e = time.perf_counter()
print(f"\n----    PART 2    ----\n")
print(f'PART 2: {part_2} in {(e - s)*1000:0.3f} ms')
print(f"\n----------------------\n")
