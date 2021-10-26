import sys
from re import findall

def lights(actions: dict, input: str):
  lights = [[0 for _ in range(1000)] for _ in range(1000)]
  instructions = findall("(toggle|turn on|turn off)\s(\d*),(\d*)\sthrough\s(\d*),(\d*)", input)
  for action, x1, y1, x2, y2 in instructions:
      coords = [(x, y) for x in range(int(x1), int(x2) + 1) for y in range(int(y1), int(y2) + 1)]
      for x, y in coords:
          lights[x][y] = actions[action](lights[x][y])
  flattened = [val for sublist in lights for val in sublist]
  return sum(flattened)

def part1(input: str):
    actions = {
        'toggle': lambda x: abs(x-1),
        'turn on': lambda x: 1,
        'turn off': lambda x: 0
    }
    return lights(actions, input)

def part2(input: str):
    actions = {
        'toggle': lambda x: x+2,
        'turn on': lambda x: x+1,
        'turn off': lambda x: x-1 if x > 0 else 0
    }
    return lights(actions, input)

f = open(sys.argv[1], 'r')
input = f.read()
f.close()
print(part1(input))
print(part2(input))

# fails:
# 855284
