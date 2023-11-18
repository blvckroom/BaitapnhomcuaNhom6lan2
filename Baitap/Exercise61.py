S = 0
n = 0
while True:
    x = float(input('Enter a value: '))
    if n == 0 and x == 0:
        print('Error')
        break
    if x == 0:
        break
    S += x
    n += 1
if n > 0:
    T = S / n
    print('The average of the values is:', T)