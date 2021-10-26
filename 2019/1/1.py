import fileinput, math
# fuel for module = floor( m / 3) - 2
modules = [int(line.strip()) for line in fileinput.input()]
p1 = sum((math.floor(module/3) - 2 for module in modules))
print(f'PART_1: {p1}')


def calcFuel(mass: int, out = 0):
  fuel = math.floor(mass/3) - 2
  if fuel <= 0: return out
  out += fuel
  return calcFuel(fuel, out)

p2 = sum((calcFuel(module) for module in modules))

print(f'PART_2: {p2}')
