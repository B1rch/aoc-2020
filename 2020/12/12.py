import numpy as np
import fileinput
import math

class V(tuple):
    '''A simple vector supporting scalar multiply and vector add'''
    def __new__ (cls, *args):
        return super(V, cls).__new__(cls, args)
    def __mul__(self,s):
        return V( *( c*s for c in self) )
    def __add__(self,s):
        return V( *( c[0]+c[1] for c in zip(self,s)) )
    def __repr__(self):
        return "V" + super(V, self).__repr__()
    def distance(self):
        return (abs(self[0]) + abs(self[1]))
    def rotateSteps(self, r):
      steps = int(r / 90)
      x,y = self
      for i in range (steps):
        x,y = y, -x
      return V(x,y)

lines = [(line[0], line[1:].strip()) for line in fileinput.input()]

print(lines)

# directions in (x,y)
# tuple of dir, next, prev
directions = [
  (V(0, 1),   1, 3),   #N
  (V(1, 0),   2, 0),   #E
  (V(0, -1),  3, 1),   #S
  (V(-1, 0),  0, 2),   #W
]

def part1():
  facing, pos = V(1,0), V(0,0)
  for face, amount in lines:
    if (face == 'F'):
      pos += facing * int(amount)
    elif (face == "R"):
      facing = facing.rotateSteps(int(amount))
    elif(face=='L'):
      facing = facing.rotateSteps(360 - int(amount))
    else:
      pos += directions[['N', 'E', 'S', 'W'].index(face)][0] * int(amount)
  return pos.distance()

def part2():
  pos = V(0,0)
  wPos = V(10, 1)
  for face, amount in lines:
    if (face == 'F'):
      pos += wPos * int(amount)
    elif (face == "R"):
      wPos = wPos.rotateSteps(int(amount))
    elif(face=='L'):
      wPos = wPos.rotateSteps(360 - int(amount))
    else:
      wPos += directions[['N', 'E', 'S', 'W'].index(face)][0] * int(amount)
  return pos.distance()


part_1 = part1()
print(f'PART 1: {part_1}')

part_2 = part2()
print(f'PART 2: {part_2}')
