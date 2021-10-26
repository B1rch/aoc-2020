import os


def main():
  data = parseInput()
  finalCount = sum(map(lambda d: len(d), data))
  #print (data)
  print (finalCount)


def parseInput() -> list[set[str]]:
  cwd = os.getcwd()
  data: list[set[str]] = []
  with open(f'{cwd}/6/data.txt') as file:
    line = file.readline()
    groupSets: list[set[str]] = []
    while line:
      if (line == "" or line == "\n"):
        data.append(set.intersection(*groupSets))
        groupSets = []
        line = file.readline()
        continue
      line = line.strip()
      groupSets.append(set(line))
      line = file.readline()
    file.close()
  return data
main()
