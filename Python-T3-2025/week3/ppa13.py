word = input()

# new_word = ''

# for i in range(len(word)-1, -1, -1):
#   new_word += word[i]

# if word == new_word:
#   print('PALINDROME')
# else:
#   print('NOT PALINDROME')

if word == word[::-1]:
  print('PALINDROME')
else:
  print('NOT PALINDROME')
