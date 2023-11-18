n = input('Enter a string to check: ')
str1 = ''
str2 = ''
for k in n:
    k = ord(k)
    if (k >= 65 and k <= 90) or (k >= 97 and k <= 122):
        k -= 32
        str1 += chr(k)
i = len(str1) - 1
while i >= 0:
    str2 += str1[i]
    i -= 1
if str1 == str2:
    print('yes')
else:
    print('no')