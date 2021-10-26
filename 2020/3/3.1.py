import os

def main():
  slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1,2]]
  data = parseInput()
  total = 1

  for x, y in slopes:
    _x, _y = x, y
    count = 0
    lineLength = len(data[_y])
    while _y <= len(data) - 1:
      count += data[_y][_x % (lineLength)]
      _y += y
      _x += x
    total *= count
  print(f'total: {total}')

def parseInput() -> list[list[bool]]:
  cwd = os.getcwd()
  data = []
  with open(f'{cwd}/3/data.txt') as file:
    line = file.readline()
    while line:
      line = line.replace('\n', '')
      data.append(list(map(lambda x: x == '#', line)))
      line = file.readline()
    file.close()
  return data
main()
