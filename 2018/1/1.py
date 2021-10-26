import numpy as np

data = np.loadtxt('2018/data/1.txt', dtype=int)
# data = [+7, +7, -2, -7, -4]
out = sum(data)
print(f'Part 1: {out}')

summed = []
currSum, i, l = 0, 0, len(data)
while True:
  currSum += data[i]
  if (currSum in summed):
    print(f'Part 2: {currSum}')
    break
  i = (i+1) % l
  summed.append(currSum)
