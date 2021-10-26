import numpy as np
import fileinput, math, sys
from itertools import chain, combinations

### UTILS

def powerset(iterable):
    s = list(iterable)  # allows duplicate elements
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def masked(i: int, mask: str, withFloating=False):
  ib = format(i, '036b')
  if (not withFloating):
    s = [x[1] if x[1] != 'X' else x[0] for x in zip(reversed(ib), reversed(mask))]
    s.reverse()
    return int(''.join(s),2)
  else:
    xs = [i for i,x in enumerate(reversed(mask)) if x == 'X']
    xsValues = [sum([2**v for v in s]) for s in powerset(xs)]
    base = ['1' if x[1] == '1' else '0' if x[1] == 'X' else x[0] for x in zip(reversed(ib), reversed(mask))]
    base = int(''.join(reversed(base)),2)
    return [base + v for v in xsValues]

### END UTILS

def part1(lines):
  mask, adresses = "", {}
  for line in lines:
    ins, value = line.split(' = ', maxsplit=1)
    if (ins == 'mask'): mask = value
    else:
      mem = ins[4:-1]
      adresses[mem] = masked(int(value), mask)
  return sum(list(adresses.values()))

def part2(lines):
  mask, adresses = "", {}
  for line in lines:
    ins, value = line.split(' = ', maxsplit=1)
    if (ins == 'mask'): mask = value
    else:
      mem = ins[4:-1]
      memList = masked(int(mem), mask, withFloating=True)
      for m in memList:
        adresses[m] = int(value)
  return sum(list(adresses.values()))

lines: list[str] = [line.strip() for line in fileinput.input()]

part_1 = part1(lines)
print(f"\n----    PART 1    ----\n")
print(f'PART 1: {part_1}')
print(f"\n----------------------\n")

part_2 = part2(lines)
print(f"\n----    PART 2    ----\n")
print(f'PART 2: {part_2}')
print(f"\n----------------------\n")
