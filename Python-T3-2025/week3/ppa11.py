num = int(input())

for x in range(1, num):
  for y in range(x, num):
    for z in range(y, num):
      if x ** 2 + y ** 2 == z**2:
        print(f'{x},{y},{z}')
