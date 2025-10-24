num1 = int(input())
num2 = int(input())

sum = 0

for num in range(1000, 2001):
  if num % num1 == 0 and num % num2 == 0:
    sum += num

print(sum)
