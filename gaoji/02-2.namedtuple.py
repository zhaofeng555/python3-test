from collections import namedtuple

p = namedtuple('Point', ['x', 'y'])
p.x, p.y = 1, 2
print(p.x + p.y)
