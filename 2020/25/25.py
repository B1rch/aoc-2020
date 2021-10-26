import itertools

test = (5764801, 17807724)
actual = (8335663, 8614349)
actualLoopSize = (6041183, 8306869) #found earlier and will never change


def doSteps(subject: int, value: int, amount = 1):
  for _ in range(amount):
    value *= subject
    value = value % 20201227
  return value

def findLoopSize(subject: int, value: int,target: int):
  for i in itertools.count(1):
    value = doSteps(subject, value)
    if value == target: return i
    if i > 100000000: return -1

# uncomment to re-find loop sizes
#out = list(map(lambda x: findLoopSize(7,1,x), test ))
key = doSteps(actual[0], 1, actualLoopSize[1])
print(f'Part_1: {key}')

