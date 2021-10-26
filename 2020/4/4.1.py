import os
import re
from typing import Dict, TypedDict

class Data(TypedDict, total=False):
  byr: str
  iyr: str
  eyr: str
  hgt: str
  hcl: str
  ecl: str
  pid: str
  cid: str

hclRe = re.compile("^#[0-9a-z]{6}$", re.M | re.I)
eclRe = re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$", re.M)
pidRe = re.compile("^[0-9]{9}$", re.M)

def main():
  data = parseInput()
  filtered = list(filter(validator, data))
  validCount = len(filtered)
  print(validCount)


def validator(dict: Data):
  if (len(dict) < 7): return False
  if (len(dict) == 7 and 'cid' in dict): return False
  if (int(dict['byr']) > 2002 or int(dict['byr']) < 1920): return False
  if (int(dict['iyr']) > 2020 or int(dict['iyr']) < 2010): return False
  if (int(dict['eyr']) > 2030 or int(dict['eyr']) < 2020): return False
  if (not checkHeight(dict['hgt'])): return False
  if (not hclRe.match(dict['hcl'])): return False
  if (not eclRe.match(dict['ecl'])): return False
  if (not pidRe.match(dict['pid'])): return False
  return True


def checkHeight(h:str) -> bool:
  config = {
    'cm': [150, 193],
    'in': [59, 76]
  }
  if (not h.endswith(('cm', 'in'))): return False
  else:
    height, unit = [h[:-2], h[-2:]]
    if (not unit in config): return False
    min, max = config[unit]
    if (int(height) < min or int(height) > max): return False
    return True


def parseInput() -> list[Data]:
  cwd = os.getcwd()
  data = []
  with open(f'{cwd}/4/data.txt') as file:
    current = 0
    line = file.readline()
    while line:
      if (line == "" or line == "\n"):
        current += 1
        line = file.readline()
        continue
      line = line.strip()
      if (len(data) == current ): data.append(Data())
      units = line.split(' ')
      for unit in units:
        name, value = unit.split(':')
        data[current][name] = value
      line = file.readline()
    file.close()
  return data
main()
