import math
p = 0
x1 = float(input('Enter the x part of the coordinate: '))
y1 = float(input('Enter the y part of the coordinate: '))
x2, y2 = x1, y1
while True:
    x = input('Enter the x part of the coordinate: (blank to quit): ')
    if x == '':
        break
    y = input('Enter the y part of the coordinate: ')
    if y == '':
        break
    x = float(x)
    y = float(y)
    distance = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
    x1 = x
    y1 = y
    p += distance
p += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print('The perimeter of that polygon is ', p)