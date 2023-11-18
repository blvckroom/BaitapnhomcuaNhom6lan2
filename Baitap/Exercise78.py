n = ''
m = int(input('Enter a decimal number: '))
while m > 0:
    r = m % 2
    n = str(r) + n
    m = m // 2
print('The binary number is:', n)