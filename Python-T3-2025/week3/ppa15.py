value = input()
is_num = False
nums = [
    0, 1,
    2, 3,
    4, 5,
    6, 7,
    8, 9,
    '.'
]

for char in value:
  if char in nums:
    is_num = True
if is_num:
  if value.count('.') == 1 in value:
    print('Float')
  elif value.count('.') == 0 in value:
    print('Integer')
  else:
    print('None')
else:
  print('None')
