import fileinput
from functools import reduce

def countBrackets(s: str) -> int:
  return reduce(lambda acc, c: acc+1 if c == "(" else acc-1, s, 0)

def firstBasement(s:str)->int:
  counts = [0,0]
  for i,c in enumerate(s):
    j = int(c == '(')
    counts[j] += 1
    if (counts[0] > counts[1]): return i+1
bracketString = fileinput.input().readline().strip()
print(f"Floor = {countBrackets(bracketString)}")
print(f"First basement = {firstBasement(bracketString)}")

