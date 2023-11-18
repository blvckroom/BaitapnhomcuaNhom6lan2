S = 0
while True:
    n = input('Item price:')
    if not n:
        break
    n = float(n)
    S += n
T = S
if T % 5 < 2.5:
    T = T - (T % 5)
else:
    T = T + (5 - (T % 5))
print('Total cost of all items:', S)
print('Amount to be paid:', T)