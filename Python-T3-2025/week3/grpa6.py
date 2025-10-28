number = int(input())

for x in range(1, number+1):
  nums = []
  for i in range(1, x+1):
    nums.append(str(i))

  print(','.join(nums))

for x in range(number-1, 0, -1):
  nums = []
  for i in range(1, x+1):
    nums.append(str(i))

  print(','.join(nums))
