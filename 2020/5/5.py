import builtins
import os
from typing import TypedDict

class Data(TypedDict):
  row: int
  col: int
  id: int

def main():
  data = parseInput()
  data.sort(key=lambda d: d['id'])
  max = maxID(data)
  myId = findSeatId(data)
  print(myId)
  print(max)

# find a gap of two in sorted list
# when id found, this is 1 higher than my id
def findSeatId(data: list[Data]) -> int:
  prev = data[0]['id']
  for d in data:
    id = d['id']
    if (id - prev == 2): return id - 1
    prev = id
  return -1

def maxID(data: list[Data]) -> int:
  max = 0
  for d in data:
    id = d['id']
    if (id >= max):
      max = id
  return max

def parseInput() -> list[Data]:
  cwd = os.getcwd()
  data = []
  with open(f'{cwd}/5/data.txt') as file:
    line = file.readline()
    while line:
      line = line.strip()
      bitString = ""
      fields: Data = {}
      for c in line:
        if (c == 'B' or c == 'R' ): bitString += '1'
        else: bitString += '0'
      row = int('0b' + bitString[:7], 2)
      col = int('0b' + bitString[7:], 2)
      fields = {
        'row': row,
        'col': col,
        'id': row * 8 + col
      }
      data.append(fields)
      line = file.readline()
    file.close()
  return data


main()
