import fileinput
import more_itertools as mi
import numpy as np
from itertools import  groupby


data = [line.strip() for line in fileinput.input()]

def isNice(s: str) -> bool:
  notHas      = not any([x in s for x in ['ab', 'cd', 'pq', 'xy']])
  hasMultiple = any([len(list(b))>=2 for _,b in groupby(s)])
  hasVowels   = sum([s.lower().count(x) for x in 'aeiou'])>=3
  return all([notHas, hasMultiple, hasVowels])

def isNicer(s:str) -> bool:
  hasPairTwice = any([s.lower().count(''.join(x))>=2 for x in zip(s, s[1:])])
  inBetween    = any([a == c for a,_,c in mi.windowed(s, 3)])
  return all([hasPairTwice, inBetween])

def part1(data: str):
  return np.count_nonzero([isNice(s) for s in data])

def part2(data:str):
  return np.count_nonzero([isNicer(s) for s in data])

print(part1(data))
print(part2(data))
