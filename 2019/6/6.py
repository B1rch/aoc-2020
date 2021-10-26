import fileinput
from collections import defaultdict, deque
from shared.helpers import dijkstra, time_decorator

@time_decorator
def day6(data):
    newData, p1 = day6_part1(data.copy())
    print(f"{'=' * 20} PART 1 {'=' * 20}")
    print(f"Total number of orbits = {p1}")
    print("\n")
    p2 = day6_part2(newData)
    print(f"{'=' * 20} PART 2 {'=' * 20}")
    print(f"Total number of hops = {p2}")

@time_decorator
# BFS with incrementing counter based on counter of parent
def day6_part1(_data):
  start = 'COM'
  Q,S = deque([start]), set([start])
  while Q:
    curr = Q.popleft()
    for edge in _data[curr][1]:
      if edge not in S:
        _data[edge][0] = _data[curr][0] + 1
        S.add(edge)
        Q.append(edge)
  return data, sum([v[0] for v in _data.values()])

@time_decorator
def day6_part2(_data):
  santaParent = '6F7'
  meParent = 'WFF' # (just ctrl+f up correct orbit in data)

  me = dijkstra(_data, 'COM', meParent)
  santa = dijkstra(_data, 'COM', santaParent)
  lastCommon = [j for i,j in zip(me, santa) if i == j][-1]
  return abs(_data[meParent][0] - _data[lastCommon][0]) + abs(_data[santaParent][0] - _data[lastCommon][0])


if __name__ == "__main__":
  data = defaultdict(lambda: [0, set()])
  for line in fileinput.input():
    a,b = line.strip().split(')')
    data[b] = data[b] if data[b] else [0, set()]
    data[a][1].add(b)
  day6(data)
