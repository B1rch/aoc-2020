from collections import defaultdict
import fileinput
import time

lines = [int(line.strip()) for line in fileinput.input()]

pSize = 25 #preamble size

def findFirstInvalid():
  nList = lines[:pSize]
  for line in lines[pSize:]:
    res = checkSum(nList, line)
    if (not res): return line
    else:
      nList = [*nList[1:],line]


def checkSum(list: list[int], target: int) -> bool:
  halveTarget = target/2
  return any([i != halveTarget and target - i in list for i in list])


def findSummingRegion(target: int) -> list[int]:
  indexTarget = lines.index(target)
  initials = [lines[:indexTarget], lines[indexTarget + 1:]]
  for initial in initials:
    result = checkContiguousSum(initial, target)
    if (result != None):
      return result

# check contiguous regions using sliding window approach
def checkContiguousSum(list: list[int], target: int) -> list[int]:
  for size in range(2, len(list)): # size of subsection
    for start in range(0, len(list) - size):
      subList = list[start:start + size-1]
      s = sum(subList)
      if (s == target): return subList
  return None #nothing found

s = time.perf_counter()
part_1 = findFirstInvalid()
e = time.perf_counter()
print(f'Part 1: {part_1} in {(e - s)*1000:0.4f} ms')

s = time.perf_counter()
part_2 = findSummingRegion(part_1)
e = time.perf_counter()
print(f'Part 2: {min(part_2) + max(part_2)} in {(e - s)*1000:0.4f} ms')
