while True:
    count = 0
    n = input('Enter 8 bits: ')
    if n == '':
        break
    for i in range(0, 8):
        if n[i] == '1':
            count += 1
    if count % 2 == 0:
        print('0')
    else:
        print('1')