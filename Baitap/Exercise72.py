n = input('Enter a string to check: ')
str1 = ''
str2 = ''
i = len(n) - 1
for k in n:
    if not k == ' ':
        str1 += k
while i >= 0:
    if not n[i] == ' ':
        str2 += n[i]
    i -= 1
if str1 == str2:
    print('yes')
else:
    print('no')