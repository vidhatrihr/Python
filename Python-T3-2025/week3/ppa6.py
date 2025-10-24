min_len = float('inf')
min_word = None

while (True):
  word = str(input())
  if word == 'abcdefghijklmnopqrstuvwxyz':
    break
  if len(word) < min_len:
    min_len = len(word)
    min_word = word

print(min_word)
