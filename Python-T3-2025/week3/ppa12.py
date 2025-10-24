string1 = input()
string2 = input()


for i in string2:
  if i in string1:
    string2 = string2.replace(i, '')

print(string2)
