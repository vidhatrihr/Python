num = int(input())

is_prime = True
primes = []
primes_sum = 0

for i in range(2, num+1):
  for j in range(2, i):
    if i % j == 0:
      is_prime = False
      break
    else:
      is_prime = True
  if is_prime:
    primes.append(i)
    primes_sum += i

print(primes_sum)
