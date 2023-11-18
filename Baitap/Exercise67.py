x = 0
S = 0
while True:
    n = input('Enter age: ')
    if not n:
        break
    n = int(n)
    if n > 0:
        if n <= 2:
            x = 0
        elif 3 <= n <= 12:
            x = 14.00
        elif n >= 65:
            x = 18.00
        else:
            x = 23.00
    S += x
print('Ticket price = {:.2f}'.format(S))