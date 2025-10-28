task = input()

if task == "sum_until_0":
  total = 0
  n = int(input())
  while n != 0:  # the terminal condition
    total += n  # add n to the total
    n = int(input())  # take the next n form the input
  print(total)

elif task == "total_price":
  total_price = 0
  while True:  # repeat forever since we are breaking inside
    line = input()
    if line == 'END':  # The terminal condition
      break
    quantity, price = line.split()  # split uses space by default
    quantity, price = int(quantity), int(price)  # convert to ints
    total_price += quantity * price  # accumulate the total price
  print(total_price)

elif task == "only_ed_or_ing":
  while True:
    word = input()
    if word == 'STOP':
      break
    elif word[-2:] == 'ed' or word[-3:] == 'ing':
      print(word)

elif task == "reverse_sum_palindrome":
  while True:
    num = int(input())
    if num == -1:
      break
    else:
      added = str(sum(list(map(int, str(num)))))
      if added == added[::-1]:
        print(num)

elif task == "double_string":
  while True:
    line = input()
    if line == '':
      break
    else:
      print(line + line)

elif task == "odd_char":
  lines = []
  while True:
    line = input()
    lines.append(line[::2])
    if line[-1] == '.':
      break
  print(' '.join(lines))

elif task == "only_even_squares":
  while True:
    num = input()
    if num == 'NAN':
      break
    if int(num) % 2 == 0:
      print(int(num)**2)

elif task == "only_odd_lines":
  count = 0
  lines = []
  while True:
    line = input()
    count += 1
    if line == 'END':
      break
    else:
      if count % 2 != 0:
        lines.append(line)
  print('\n'.join(lines[::-1]))
