import random
x = random.randint(1, 100)
i = 1
count = 0
max_value = x
print(x, end='\n')
while i <= 100:
    x = random.randint(1, 100)
    print(x, end='\n')
    if max_value < x:
        max_value = x
        count += 1
    i += 1
print('max =', max_value, end='\n')
print(f'found max after {count} updates')