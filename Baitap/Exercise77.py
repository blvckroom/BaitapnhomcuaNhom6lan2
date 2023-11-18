n = input('Enter a binary number: ')
m = 0
for i in range(len(n)):
    x = int(n[i])
    m += x * (2 ** (len(n) - 1 - i))
print('The decimal number is:', m)