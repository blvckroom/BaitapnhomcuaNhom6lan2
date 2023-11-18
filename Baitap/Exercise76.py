n = int(input('Enter an integer: '))
if n < 2:
    print('Error!!')
else:
    factor = 2
    while factor <= n:
        if n % factor == 0:
            print(factor)
            n //= factor
        else:
            factor += 1