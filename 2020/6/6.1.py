import os


def main():
  data = parseInput()
  finalCount = sum(map(lambda d: len(d), data))
  print (finalCount)


def parseInput() -> list[set[str]]:
  cwd = os.getcwd()
  data: list[set[str]] = []
  with open(f'{cwd}/6/test.txt') as file:
    data.append(set())
    line = file.readline()
    while line:
      if (line == "" or line == "\n"):
        data.append(set())
        line = file.readline()
        continue
      line = line.strip()
      for c in line: data[len(data)-1].add(c)
      line = file.readline()
    file.close()
  return data
main()
