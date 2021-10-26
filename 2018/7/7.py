import fileinput, time
from collections import defaultdict
import numpy as np
from anytree import Node, RenderTree

def makeNodes(letters):
  _l = np.array(letters)
  starts = sorted(set(_l[:,0]).difference(set(_l[:,1])))
  nodes = defaultdict(lambda: {'incoming': set(), 'outgoing': set()})
  for a,b in letters:
    nodes[a]['outgoing'].add(b)
    nodes[b]['incoming'].add(a)
  return nodes, starts

def part1(letters):
  nodes, starts = makeNodes(letters)

  l = []
  s = set(starts)
  while len(s) != 0:
    toRemove = min(s, key=ord)
    s.remove(toRemove)
    l.append(toRemove)
    for node in sorted(nodes[toRemove]['outgoing']):
      nodes[node]['incoming'].remove(toRemove)
      if len(nodes[node]['incoming']) == 0:
        s.add(node)
  return ''.join(l)

def part2(letters):
  return 2



lines = [line.strip() for line in fileinput.input()]
letters  = [[x[5],x[36]] for x in lines]

s = time.perf_counter()
part_1= part1(letters)
e = time.perf_counter()
print(f"\n----    PART 1    ----\n")
print(f'PART 1: {part_1} in {(e - s)*1000:0.3f} ms')
print(f"\n----------------------\n")

s = time.perf_counter()
part_2 = part2()
e = time.perf_counter(letters)
print(f"\n----    PART 2    ----\n")
print(f'PART 2: {part_2} in {(e - s)*1000:0.3f} ms')
print(f"\n----------------------\n")
