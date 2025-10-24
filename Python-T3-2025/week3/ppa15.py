value = input()

try:
  type(int(value)) == int
  print('Integer')

except ValueError:
  print(isinstance(int(value), float))
