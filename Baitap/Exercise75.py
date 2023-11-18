m = int(input('Enter m: '))
n = int(input('Enter n: '))
if n < m:
    d = n
else:
    d = m
while d > 0:
    if n % d == 0 and m % d == 0:
        break
    d -= 1
print('The greatest common divisor is:', d)