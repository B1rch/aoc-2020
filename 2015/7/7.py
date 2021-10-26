import fileinput
from collections import defaultdict
from typing import DefaultDict, Union

def ti(s:str):
  return int(s) if s.isnumeric() else s

def get(v: Union[int,str], wires: dict):
  return v if isinstance(v, int) else wires[v]

actions = {
  'NOT'   : lambda   x:   ~ x,
  'AND'   : lambda x,y: x & y,
  'OR'    : lambda x,y: x | y,
  'LSHIFT': lambda x,y: x << y,
  'RSHIFT': lambda x,y: x >> y,
}

wires = defaultdict(None)
for line in fileinput.input():
  left, right = line.strip().split(' -> ')
  if left.count(" ") == 0:
    wires[right] = ti(left)
  elif 'NOT' in left:
    wires[right] = ('NOT', ti(left))
  else:
    x,y,z = left.split(' ')
    wires[right] = (y,ti(x), ti(z))

def solveFor(tree, node):
  expr = tree[node]
  if isinstance(expr, int): return expr
  elif isinstance(expr, str): return solveFor(tree, expr)
  else:
    op, params = expr[0], expr[1:]
    return actions[op](*[solveFor(x) if isinstance(x, str) else x for x in params])


