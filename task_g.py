import re

test_str = input()

fig = "\d+"

match = re.findall(fig, test_str)
match = [int(x) for x in match]
test_str = re.sub(fig, '', test_str)
n = sum(match) - len(match) + len(test_str)
print(n)