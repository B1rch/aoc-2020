# import itertools as it
# import more_itertools as mi
import numpy as np
import fileinput
from collections import defaultdict

def buildGuardSleepSchedule(data):
  schedule = defaultdict(lambda: (0, []))

  currGuard = -1
  sleepTime = 0
  for d in data:
    time, action = d[15:17], d[19:24]
    if (action == 'Guard'):
      currGuard = int(d[26:].split(' ', maxsplit=1)[0])
      continue
    if (action == 'falls'):
      sleepTime = int(time)
      continue
    if (action == 'wakes'):
      sleepRange = sum([schedule[currGuard][0],int(time) - sleepTime])
      newMinutes = [*schedule[currGuard][1], *[i for i in range(sleepTime,int(time))]]
      schedule[currGuard] = (sleepRange, newMinutes)
      continue
  return schedule

def part1(data):
  schedule = buildGuardSleepSchedule(data)
  bestId = max(schedule.items(), key=lambda x: x[1][0])[0]
  bestMinute = max([*zip(*np.unique(schedule[bestId][1], return_counts=True))], key=lambda x: x[1])[0]
  return bestId * bestMinute

def part2(data):
  # inefficient as all fuck, but who cares
  schedule = buildGuardSleepSchedule(data)
  bestId = max(schedule.items(), key=lambda x: max([*zip(*np.unique(x[1][1], return_counts=True))], key=lambda x: x[1])[1])[0]
  bestMinute = max([*zip(*np.unique(schedule[bestId][1], return_counts=True))], key=lambda x: x[1])[0]
  return bestId * bestMinute


data = [line.strip() for line in fileinput.input()]

data = sorted(data)

part_1 = part1(data)
print(f"\n----    PART 1    ----\n")
print(f'PART 1: {part_1}')
print(f"\n----------------------\n")

part_2 = part2(data)
print(f"\n----    PART 2    ----\n")
print(f'PART 2: {part_2}')
print(f"\n----------------------\n")
