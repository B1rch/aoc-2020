import fileinput, sys
from collections import defaultdict
from copy import deepcopy

def parseInput():
  file = open(sys.argv[1])
  try:
    d1,d2 = (list(map(int,lines[10:].split('\n'))) for lines in file.read().rstrip().split('\n\n'))
  finally:
    file.close()
  return d1,d2

def sumCards(deck: list[int]):
  return sum(map(lambda x: (x[0]+1) * x[1], enumerate(reversed(deck))))


def part1(d1: list[int], d2: list[int]):
  while d1 and d2:
    c1,c2 = d1.pop(0), d2.pop(0)
    if (c1 == c2):
      raise ValueError('Undefined behaviour if equal: ', c1, c2)
    elif (c1 > c2):
      d1.extend([c1,c2])
    else:
      d2.extend([c2,c1])
  return max(map(sumCards, [d1,d2]))

def recursiveGame(d1: list[int],d2: list[int], config, round=0) -> int:
  print(f'In game: {round}')
  config[round] = [set(),set()] #clearing seen configurations on round start
  while d1 and d2:
    if ('.'.join(map(str, d1)) in config[round][0] and '.'.join(map(str, d2)) in config[round][1]):
      return sumCards(d1) if not round else 1
    config[round][0].add('.'.join(map(str, d1)))
    config[round][1].add('.'.join(map(str, d2)))
    c1,c2 = d1.pop(0), d2.pop(0)
    if (c1 <= len(d1) and c2 <= len(d2)):
      p1win = recursiveGame([*d1[:c1]], [*d2[:c2]],config, round + 1)
      if p1win: d1.extend([c1,c2])
      else: d2.extend([c2,c1])
    elif (c1 > c2):
      d1.extend([c1,c2])
    else:
      d2.extend([c2,c1])
  return max(map(sumCards, [d1,d2])) if not round else int(bool(len(d1)))

def part2(d1: list[int], d2: list[int]):
  config = defaultdict(lambda: [set(),set()])
  return recursiveGame(d1,d2, config, 0)

d1, d2 = parseInput()
p1= part1([*d1],[*d2])
print('PART_1:', p1)
p2 = part2([*d1],[*d2])
print('PART_2:', p2)
