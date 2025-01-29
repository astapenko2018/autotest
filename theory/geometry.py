from theory.point import *

# l1 = [Point(3, 1), Point(0, 0), Point(1, 2)]
#
#
# l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))
#
# print(l1)
# print(l2)

l = []

for i in range(-5, 6):
    l.append(Point(i, i*i))

l2 = []
for el in l:
    l2.append(Point(el.x, el.y))

print(l)
print(l2)
