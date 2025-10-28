marks = int(input())
no_of_opt = int(input())
correct_opt = list(map(int, input().split(',')))
chosen_opt = list(map(int, input().split(',')))

scored = 0

for opt in chosen_opt:
  if opt not in correct_opt:
    scored = 0.0
  else:
    scored += marks / len(correct_opt)

print(scored)
