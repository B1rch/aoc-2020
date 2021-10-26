import numpy as np
import fileinput, math, sys
from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

lines = [line.strip() for line in fileinput.input()]

timestamp, buses = int(lines[0]), [(i, int(bus)) for i, bus in enumerate(lines[1].split(',')) if bus != 'x']

def part1():
  minWait, minId = sys.maxsize, None
  #return min([math.ceil(timestamp/t) * t - timestamp for t in data])
  for _,t in buses:
    c = math.ceil(timestamp/t) * t - timestamp
    if (c < minWait):
      minWait, minId = c, t
  return minId * minWait

def part2():
  dividers = [bus for _, bus in buses]
  remainders = [bus - i for i, bus in buses]
  return chinese_remainder(dividers, remainders)


part_1 = part1()
print(f"\n----    PART 1    ----\n")
print(f'PART 1: {part_1}')
print(f"\n----------------------\n")

part_2 = part2()
print(f"\n----    PART 2    ----\n")
print(f'PART 2: {part_2}')
print(f"\n----------------------\n")
