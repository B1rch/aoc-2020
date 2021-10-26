import sys

rulesdata, stringsdata = open(sys.argv[1], 'r').read().split('\n\n')
strings = stringsdata.split('\n')
rules = {}
for line in rulesdata.split('\n'):
    k, rule = line.split(': ')
    if rule[0] == '"':
        rule = rule[1:-1]
    else:
        rule = [seq.split(' ') if ' ' in seq else [seq]
                for seq in (rule.split(' | ') if ' | ' in rule else [rule])]
    rules[k] = rule

def run_seq(g, seq, s):
    if not seq:
        yield s
    else:
        k, *seq = seq
        for s in run(g, k, s):
            yield from run_seq(g, seq, s)

def run_alt(g, alt, s):
    for seq in alt:
        yield from run_seq(g, seq, s)

def run(g, k, s):
    if isinstance(g[k], list):
        yield from run_alt(g, g[k], s)
    else:
        if s and s[0] == g[k]:
            yield s[1:]

def match(g, s):
    return any(m == '' for m in run(g, '0', s))

print('P1', sum(match(rules, s) for s in strings))
rules = {**rules, '8': [['42'], ['42', '8']], '11': [['42', '31'], ['42', '11', '31']]}
print('P2', sum(match(rules, s) for s in strings))
