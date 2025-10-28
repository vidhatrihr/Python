value = int(input())

sum = 0
for i in range(1, value+1):
  for j in range(1, i+1):
    sum += j

print(sum)
