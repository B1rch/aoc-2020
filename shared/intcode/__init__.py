from collections import deque
from shared.event import Event
from typing import Union

def readOpcode(s):
  return [int(i) for i in s.strip().split(',')]

class Intcode():
  def __init__(self, mem: list[int]) -> None:
      self.memory = mem.copy()
      self.paused = False
      self.BOUNDS = (0, len(mem)-1)
      self.pointer = 0
      self.input = deque()
      self.events = {
        'onInput': Event(),
        'onOutput': Event(),
        'onExit': Event()
      }
      self.pModes = []
      self.out = []
      self.relativebase = 0
      self.pointerMod = False
      self.opcodes = {
        99: ( 0, (
              lambda        : self.exit()
          )),
        1:  ( 3, (
              lambda   x,y,z: self.add(x,y,z)
          )),
        2:  ( 3, (
              lambda   x,y,z: self.mul(x,y,z)
          )),
        3:  ( 1, (
              lambda address: self.readInput(address)
          )),
        4:  ( 1, (
              lambda address: self.output(address)
          )),
        5:  ( 2, (
              lambda a,b: self.jmp(lambda x: x != 0,a,b)
          )),
        6:  ( 2, (
              lambda a,b: self.jmp(lambda x: x == 0,a,b)
          )),
        7:  ( 3, (
              lambda a,b,address: self.cmp(lambda x,y: x < y,a,b, address)
          )),
        8:  ( 3, (
              lambda a,b,address: self.cmp(lambda x,y: x == y,a,b, address)
          )),
        8:  ( 1, (
              lambda a: self.adjustRelBase(a)
          )),
      }

  def jmp(self, pred, value:int, dest: int) -> None:
    if pred(self.value(value, self.pModes[0])):
      self.pointerMod = True
      self.pointer = self.value(dest, self.pModes[1])

  def cmp(self, pred, v1:int, v2:int, address:int, trueValue:int = 1, falseValue:int = 0) -> None:
      self.memory[address] = trueValue if pred(self.value(v1, self.pModes[0]),self.value(v2, self.pModes[1])) else falseValue

  def output(self, address)-> None:
    v = self.value(address, self.pModes[0])
    self.out.append(v)
    self.events['onOutput'](v)

  def readInput(self, address:int):
    handler = lambda : self.cnt()
    if (not len(self.input)):
      self.events['onInput'] += handler
      self.pause()
    else:
      self.setAddress(address, self.input.popleft())

  def value(self, address, mode = 0) -> int:
    if    mode == 0: return self.memory[address]
    elif  mode == 1: return             address
    elif  mode == 2: return self.memory[address + self.relativebase]

  def next(self, amount: int = 1) -> None:
    self.pointer += amount

  def add(self,a: int,b: int,address: int) -> None:
    self.memory[address] = self.value(a,self.pModes[0]) + self.value(b,self.pModes[1])

  def mul(self,a: int,b: int,address: int) -> None:
    self.memory[address] = self.value(a,self.pModes[0]) * self.value(b,self.pModes[1])

  def setAddress(self, address: int, input: int) -> None:
    self.memory[address] = input

  def exit(self) -> int:
    return self.value(0)

  def memRange(self, start: int, len: int) -> list[int]:
    return self.memory[start:start+len]

  def setmem(self, mem: list[int]) -> None:
    self.memory = mem

  def adjustRelBase(self, adjustment: int):
    self.relativebase += self.value(adjustment, self.pModes[0])

  def setInput(self, inputs: Union[int, list[int]]):
    if isinstance(inputs, int): inputs = [inputs]
    self.events['onInput']()
    self.input.extend(inputs)

  def pause(self):
    self.paused = True

  def cnt(self):
    self.paused = False
    self.run(self.pointer)

  def doOpCode(self, pointer: int) -> Union[int, None]:
    # pause if needed (exit out, start back later using cnt())
    if self.paused: return 'p'

    # reset pointerMod
    self.pointerMod = False
    # parse opcode as string, last two values are actual opcode
    s = str(self.memory[pointer])
    params, code = s[:-2] , int(s[-2:])

    # get amount of params and func to execute
    nArgs, func = self.opcodes[code]

    # build list of parameter modes. Need to pad left with 0 if opcode has leading zeros
    # reversed because pmodes are read right -> left
    self.pModes = [int(x) for x in "0" * (nArgs - len(params)) + params][::-1]

    # run code and return if needed
    exitCode = func(*self.memRange(self.pointer + 1, nArgs))
    if exitCode: return exitCode

    # increment pointer by amount of parameters
    if not self.pointerMod: self.pointer += nArgs + 1


  def run(self, pointer = 0) -> Union[tuple[int, list[int]], None]:
    self.pointer = pointer
    while True:
      exitCode = self.doOpCode(self.pointer)
      if exitCode:
        self.events['onExit'](exitCode)
        return exitCode, self.out
