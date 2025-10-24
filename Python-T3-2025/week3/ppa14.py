num1 = int(input())
num2 = int(input())

is_coprime = True
for i in range(2, min(num1, num2)):
  if num1 % i == 0 and num2 % i == 0:
    is_coprime = False
  break

if is_coprime:
  print('coprime')
else:
  print('Not coprime')
