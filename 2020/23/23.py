from dataclasses import dataclass, field


@dataclass
class Cup:
    value: int
    next_cup: "Cup" = field(repr=False)

    def __init__(self, val, next_cup=None):
        self.value = int(val)
        self.next_cup = next_cup

data = list('624397158')
cups = {}

last_cup = Cup(data.pop(0))
first_cup = last_cup
cups[last_cup.value] = last_cup
for c in data:
    cup = Cup(c)
    last_cup.next_cup = cup
    cups[cup.value] = cup
    last_cup = cup
last_cup.next_cup = first_cup


def rotate_cups(first_cup, cups, rotations):
    cup = first_cup
    for _ in range(rotations):
        a = cup.next_cup
        b = a.next_cup
        c = b.next_cup
        dest = cup.value - 1
        while True:
            if dest in [a.value, b.value, c.value]:
                pass
            elif dest < 0:
                dest = max(cups.keys())
                continue
            elif dest in cups:
                dest_cup = cups[dest]
                break
            dest -= 1
        break_cup = dest_cup.next_cup
        cup.next_cup = c.next_cup
        dest_cup.next_cup = a
        c.next_cup = break_cup
        cup = cup.next_cup

    return cups


cups = rotate_cups(first_cup, cups, 100)
cup = cups[1]
ans = []
for _ in range(len(cups)):
    ans.append(cup.value)
    cup = cup.next_cup
ans.pop(0)
print('Part 1:', ''.join(map(str, ans)))


data = list('624397158')
cups = {}

last_cup = Cup(data.pop(0))
first_cup = last_cup
cups[last_cup.value] = last_cup
for c in data:
    cup = Cup(c)
    last_cup.next_cup = cup
    cups[cup.value] = cup
    last_cup = cup
for c in range(max(cups.keys())+1, 1000001):
    cup = Cup(c)
    last_cup.next_cup = cup
    cups[cup.value] = cup
    last_cup = cup
last_cup.next_cup = first_cup

cups = rotate_cups(first_cup, cups, 10000000)
cup1 = cups[1].next_cup
cup2 = cup1.next_cup
print("Part 2:", cup1.value * cup2.value)
