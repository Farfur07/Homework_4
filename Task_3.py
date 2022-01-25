import math
x = int(input('x= '))
y = int(input('y= '))

r = 4

point = abs(math.sqrt(x**2 + y**2))

if point <= r:
    print('point in circle')
else:
    print('point not in circle')

