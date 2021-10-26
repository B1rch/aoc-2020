import sys, os
sys.path.append(f'{os.getcwd()}/')

import fileinput
from shared.intcode import Intcode

data = [int(i) for i in fileinput.input().readline().strip().split(',')]

# comment for testing
data[1] = 12
data[2] = 2

ic = Intcode(data)
out, _ = ic.run()

print(f'PART_!: {out}')


def part2():
  target = 19690720
  for i in range(100):
    for j in range(100):
      ic.setmem([data[0], i, j, *data[3:]])
      out, _ = ic.run()
      if out == target:
        return i,j
  return -1, -1

noun, verb = part2()
print(f'PART_2: {100 * noun + verb}')


# expected output: 4090701, 6421
