value = int(input())

primes = []

for val in range(2, value):
  for x in range(2, val):
    if val % x == 0:
      break
    else:
      if val not in primes:
        primes.append(val)

print([prime for prime in primes if value % prime == 0])
