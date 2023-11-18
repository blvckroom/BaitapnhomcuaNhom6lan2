print('Celsius ----------> Fahrenheit.')
for c in range(0,100,10):
    f = 9*c/5 + 32
    c = str(c).rjust(2)
    f = str(f).rjust(2)
    print(f'{c}---------->{f}')
