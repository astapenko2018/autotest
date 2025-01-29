l = [1, 2, 3, 4, 5]

print(len(l), type(l))
new = l[0] = 10
print(l)


t = (1, 2, 3, 4, 5)
print(t[0])
new = t[0] = 10
print(t)
print(len(t), type(t))
