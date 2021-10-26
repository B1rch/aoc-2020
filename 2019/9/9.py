import fileinput
from shared.intcode import Intcode, readOpcode
from shared.helpers import print_decorator

parseInput = readOpcode

@print_decorator
def part_1():
  print(1)


def part_2():
  print(2)

opcode = readOpcode(fileinput.input.readline())
