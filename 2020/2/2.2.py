import os
from typing import Dict, TypedDict

class D(TypedDict):
  pos1: int
  pos2: int
  char: str
  passw: str

def main():
  cwd = os.getcwd()
  count = 0
  with open(f'{cwd}/2/data.txt') as file:
    line = file.readline()
    while line:
      parsed = parseInputLine(line)
      count += isValid(parsed)
      line = file.readline()
    print(f'valid count = {count}')
    file.close()

def parseInputLine(line: str) -> D:
  split = line.replace('\n', '').split(' ')
  dict: D = {
    "pos1": int(split[0].split('-')[0]),
    "pos2": int(split[0].split('-')[1]),
    "char": split[1][0],
    "passw": split[2]
  }
  return dict

def isValid(dict: D) -> bool:
  substr = dict['passw'][dict['pos1'] - 1] + dict['passw'][dict['pos2'] - 1]
  return substr.count(dict['char']) == 1

main()
