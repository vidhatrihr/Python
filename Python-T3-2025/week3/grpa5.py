value = input()

is_valid = True

if len(value) != 10:
  is_valid = False

if value[0] not in '6789':
  is_valid = False

for x in value:
  if value.count(x) > 7:
    is_valid = False
  if x*6 in value or x*7 in value:
    is_valid = False

if is_valid:
  print('valid')
else:
  print('invalid')
