from shared.vector import Vector
import fileinput

directions = {
  '>': Vector(1,0),
  'v': Vector(0,-1),
  '<': Vector(-1,0),
  '^': Vector(0,1),
}

data = [s for s in fileinput.input().readline().strip()]

def part1(data):
  S, pos = set([(0,0)]), Vector(0,0)

  for c in data:
    pos += directions[c]
    S.add(tuple(pos))
  print(f"Amount of houses = {len(S)}")

def part2(data):
  S, pos = set([(0,0)]), [Vector(0,0), Vector(0,0)]

  for i,c in enumerate(data):
    j = i%2 == 0
    pos[j] += directions[c]
    S.add(tuple(pos[j]))
  print(f"Amount of houses = {len(S)}")

part1(data)
part2(data)
