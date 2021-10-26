import numpy as np
from collections import defaultdict
import fileinput
import re

lines = [line.strip().replace(' ', '') for line in fileinput.input()]

def getParen(input: str)-> list[list[int]]:
  if not '(' in input: return []
  tmp, ps = [],[]
  for i,c in enumerate(input):
    if c == '(': tmp.append(i)
    if c == ')':
      tmp.append(i)
      ps.append([*reversed([tmp.pop(), tmp.pop()])])
  return ps[0]

# 2*3+(4*5)
# def solve(input: str) -> int:
#   ps = getParen(input)
#   opPos = [(input[m.start()], m.start()) for m in re.finditer('(\*|\+)', input)]
#   out = 0
#   for i, pos in enumerate(opPos):
#     print(pos)
def solve(input: str, plusPre=False) -> int:
  ps = getParen(input)
  while ps:
    res = solve(input[ps[0]+1:ps[1]], plusPre)
    input = ''.join([*input[:ps[0]],str(res),input[ps[1]+1:]])
    ps = getParen(input)
  nms = [*reversed(re.findall('\d+', input))]
  ops = re.findall('(\*|\+)', input)
  if plusPre:
    nms = [*reversed(nms)]
    while np.any([np.array(ops) == '+']):
      iPlus = ops.index('+')
      ops.pop(iPlus)
      a,b = int(nms.pop(iPlus)), int(nms.pop(iPlus))
      nms.insert(iPlus, a+b)
    return nms[0] if len(nms) < 2 else np.product([*map(int, nms)])
  else:
    for op in ops:
      a,b = int(nms.pop()),int(nms.pop())
      res = a * b if op == '*' else a + b
      if (len(nms) == 0):
        return res
      else:
        nms.append(res)

solve(lines[-1], True)

print(sum((solve(line) for line in lines)))
print(sum((solve(line, plusPre=True) for line in lines)))
