import os
from typing import Dict, TypedDict

class D(TypedDict):
  min: int
  max: int
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
    "min": int(split[0].split('-')[0]),
    "max": int(split[0].split('-')[1]),
    "char": split[1][0],
    "passw": split[2]
  }
  return dict

def isValid(dict: D) -> bool:
  charcount = dict['passw'].count(dict['char'])
  return charcount >= dict['min'] and charcount <= dict['max']

main()
