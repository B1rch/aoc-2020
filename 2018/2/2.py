from itertools import groupby
import itertools as it
import numpy as np
import fileinput

test=[
"abcdef",
"bababc",
"abbcde",
"abcccd",
"aabcdd",
"abcdee",
"ababab"
]

data = [line.strip() for line in fileinput.input()]
out = (0, 0)

# Part 1
for line in data:
  counts = np.unique(list(line), return_counts=True)[1]
  out = np.sum([out, (np.any(counts == 2), np.any(counts == 3))], axis=0)

print(f'Part_1: {np.product(out)}')

for x in data:
  for y in data:
    diff = 0
    for i in range(len(x)):
      if x[i] != y[i]:
        diff += 1
    if diff == 1:
      ans = []
      for i in range(len(x)):
        if x[i] == y[i]:
          ans.append(x[i])
      print (''.join(ans))
      print (x,y)
