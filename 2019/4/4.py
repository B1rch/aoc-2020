from collections import defaultdict
import numpy as np

from shared.helpers import time_decorator

def rules(i: int, groupMatching = False) -> bool:
  s,sames = str(i), defaultdict(int)
  z = zip(s, s[1:])
  for a,b in z:
    if b < a: return False
    if b == a: sames[a] += 1
  return any([v == 1 if groupMatching else v >= 1 for v in sames.values()])

@time_decorator
def day4(range: range):
    print(f"{'=' * 20} PART 1 {'=' * 20}")
    amount = day4_part1(range)
    print(f"Amount of valid passwords = {amount}")

    print(f"{'=' * 20} PART 2 {'=' * 20}")
    amount = day4_part2(range)
    print(f"Amount of valid passwords = {amount}")

@time_decorator
def day4_part1(r: range) -> int:
  return len([i for i in r if rules(i)])


@time_decorator
def day4_part2(r: range) -> int:
    return len([i for i in r if rules(i, True)])


if __name__ == "__main__":
  range = range(367479, 893699)
  # range = range(220, 225)
  day4(range)
