num1 = int(input())

prime = False
for i in range(2, num1-1):
  if num1 % i != 0:
    prime = True
  else:
    break

if prime:
  print('PRIME')
else:
  print('NOT PRIME')
