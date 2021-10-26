from os import X_OK
from shared.helpers import time_decorator
from shared.intcode import Intcode, readOpcode
import itertools as it
testOutputs = [43210, 54321, 65210]
testCodes = [[
  3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0
], [
  3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0
], [
  3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
]]

@time_decorator
def day7(amps: list[Intcode]):
  maxSignal, bestSequence = day7_part1(amps)
  print(f"{'=' * 20} PART 1 {'=' * 20}")
  print(F"Best signal = {maxSignal} with sequence {bestSequence}\n")
  maxSignal, bestSequence = day7_part2(amps)
  print(f"{'=' * 20} PART 2 {'=' * 20}")
  print(F"Best signal = {maxSignal} with sequence {bestSequence}\n")

@time_decorator
def day7_part1(amps: list[Intcode]):
  max, bestPhase = -1, None #should be low enough I guess
  for phaseSetting in it.permutations([0,1,2,3,4]):
    prevOut = 0
    for i, amp in enumerate(amps):
      amp.setInput([phaseSetting[i], prevOut])
      _, out = amp.run()
      prevOut = out[-1]
      if prevOut > max:
        max = prevOut
        bestPhase = phaseSetting
  return max, bestPhase

def cmpBest(x, max):
  if x > max:
    max = x
@time_decorator
def day7_part2(amps: list[Intcode]):
  max, bestPhase = -1, None
  handler = lambda out: amps[(i+1 % 4)].setInput(out)
  for phaseSetting in it.permutations([0,1,2,3,4]):
    for i,amp in enumerate(amps):
      # set initial input
      amp.setInput(phaseSetting[i])
      # set input of next amp to output of current
      amp.events['onOutput'] += handler
    for i,amp in enumerate(amps):
      # start amps
      _, out = amp.run()
      if i == 4 and out[-1] > max:
        max = out[-1]
        bestPhase = phaseSetting

  return max, bestPhase




if __name__ == "__main__":
  opcode = readOpcode()
  # opcode = testCodes[1]
  amps = [Intcode(opcode) for amp in 'ABCDE']
  day7(amps)
