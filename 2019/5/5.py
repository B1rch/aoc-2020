import fileinput
from typing import Union
import numpy as np
from shared.intcode import Intcode
from shared.helpers import time_decorator

@time_decorator
def day5(data: list[int]):
    print(f"{'=' * 20} PART 1 {'=' * 20}")
    _, out = day5_part1(data)
    print(f"diagnostic code = {out[-1]}")

    print(f"{'=' * 20} PART 2 {'=' * 20}")
    _, out = day5_part2(data)
    print(f"diagnostic code = {out[-1]}")

@time_decorator
def day5_part1(init: list[int]) -> Union[tuple[int, list[int]],None]:
  ic = Intcode(init)
  ic.setInput(1)
  return ic.run()


@time_decorator
def day5_part2(init: list[int]) -> int:
  ic = Intcode(init)
  ic.setInput(5)
  return ic.run()


if __name__ == "__main__":
  data = [int(i) for i in fileinput.input().readline().strip().split(',')]
  day5(data)
