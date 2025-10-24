max = 0

while (True):
  num = int(input())
  if max < num:
    max = num
  if num == 0:
    break

print(max)
