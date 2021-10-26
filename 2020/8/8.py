from collections import defaultdict
import fileinput

lines = [line.split() for line in fileinput.input()]

visited = defaultdict(dict) # list of visited instructions
def runCode():
  acc = 0 # accumulator value
  mem = 0 # pointer to current mem address
  while True:
    if (visited[mem]):
      return [-1, acc]
    elif (mem >= len(lines)):
      return [0, acc]
    ins = lines[mem][0]
    val = int(lines[mem][1])
    visited[mem] = (ins, val)
    if (ins == 'nop'):
      mem += 1
    elif (ins == 'acc'):
      acc += val
      mem += 1
    elif (ins == 'jmp'):
      mem += val

def fixCode():
  changed = set() #list of changed instructions
  lastChangedCopy = (-1 , [])
  while True:
    visited.clear()
    res = runCode()
    if (lastChangedCopy[0] >= 0):
      lines[lastChangedCopy[0]] = lastChangedCopy[1] # reset last change
      lastChangedCopy = (-1, [])
    if (res[0] == -1):#error
      # inverseInsKeys = range(len(lines), 0)
      for key in range(len(lines)-1, 0, -1):
        ins, val = lines[key]
        if (key not in changed and ((ins == 'nop' and val != 0) or ins == 'jmp')):
          lastChangedCopy = (key, lines[key]) #keep track of last change
          changed.add(key) # keep track of all changes to avoid dupes
          lines[key] = ['nop' if ins == 'jmp' else 'jmp', lines[key][1]]
          print(f'||| Changed line {key}')
          break

    elif(res[0] == 0): #found value
      return res



part_1 = runCode()
print(f"Part 1: {part_1[1]}")

part_2 = fixCode()
print(f"Part 2: {part_2[1]}")

