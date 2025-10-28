direction = input()
x = 0
y = 0

while direction != 'STOP':
  direction = input()
  if direction == 'RIGHT':
    x += 1
  elif direction == 'LEFT':
    x -= 1
  elif direction == 'UP':
    y += 1
  elif direction == 'DOWN':
    y -= 1

print(abs(x) + abs(y))
