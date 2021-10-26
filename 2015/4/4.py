from itertools import count
from hashlib import md5

data = "ckczppom"
test = "abcdef"

def part1(data: str):
  for i in count():
    if md5((data + str(i)).encode()).hexdigest().startswith('00000'):
      return i

def part2(data):
  for i in count():
    if md5((data + str(i)).encode()).hexdigest().startswith('000000'):
      return i

print(part1(data))
print(part2(data))
