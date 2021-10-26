import numpy as np

# Load data
data = np.loadtxt('10/data.txt', dtype=int)
data = np.array(sorted([0, *data, max(data) + 3]))

# get diff, count uniques, multiply them
# There's never a diff of 2 in the data, so we can use mult the result of np.unique
d = np.diff(data)
unqiues = np.unique(d, return_counts=True)
print("Part One: {}".format(np.product(np.unique(d, return_counts=True)[1])))

# RLE only the 1's in the list of diffs
def rle_ones(list: list[int]):
  count = 0
  out = []
  for i in list:
    if(i == 1):
      count += 1
    else:
      out.append(count)
      count = 0
  out.append(count)
  return out


runs = rle_ones(d)
# runs of  can have runLength - 1 of their memebers changed around,
# giving 2^(runLength-1) combinations per run, mult them together for answer.
# runs of 4 cannot use all combinations (specifically, can't use null combination)
# so substract one from combination amount using bool to int conversion
print(f"Part Two: {np.product([2**(x-1) - (x > 3) for x in runs if x])}")
