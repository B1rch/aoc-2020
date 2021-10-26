import fileinput
from collections import defaultdict
from copy import deepcopy

def parseInput():
  data = [(split[0].split(), split[1].split(', ')) for split in (line.strip()[:-1].split(' (') for line in fileinput.input())]
  return data

def part1(input):
  data = deepcopy(input)
  mightContain = defaultdict(set)
  for ingr, all in data:
    s = set(ingr)
    for allergy in all:
      if not len(mightContain[allergy]):
        mightContain[allergy] |= s
      else: mightContain[allergy] &= s

  knownAllergens = set((v for s in mightContain.values() for v in s))
  return(sum((len(set(d[0]).difference(knownAllergens)) for d in data)), mightContain)

def part2(mightContain):
  mc = deepcopy(mightContain)
  seen = set()
  while not all(map(lambda x: len(x) == 1, mc.values())):
    for value in mc.values():
      if len(value) == 1:
        seen |= value
      else:
        value -= seen
  return(','.join([next(iter(i[1])) for i in sorted(mc.items(), key=lambda x: x[0])]))

data = parseInput()
p1, mc = part1(data)
print('PART_1:', p1)
p2 = part2(mc)
print('PART_2:', p2)
