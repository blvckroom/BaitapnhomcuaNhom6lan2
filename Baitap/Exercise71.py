import math
x = float(input('Enter x = '))
guess = x/2
while abs(guess*guess - x) > pow(10,-12):
  guess = (guess + x/guess)/2
print('Square root of',x,'=',guess)