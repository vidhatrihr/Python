# L = 4
# word = input()
# space = ' '  # there is a single space
# if len(word) < L:
#   word = 'short' + space + word
# elif L <= len(word) < 2 * L:
#   word = 'medium' + space + word
# else:
#   word = 'long' + space + word
# print(word)


# while True:
#   word = input()
#   if word == 'STOP':
#     break
#   elif word[-3:] == 'ing' or word[-2:] == 'ed':
#     print(word)

x = 0
b = 10
while True:
  if x < 10:
    x = int(input())
    continue
  elif b < x < b + 2:
    break
