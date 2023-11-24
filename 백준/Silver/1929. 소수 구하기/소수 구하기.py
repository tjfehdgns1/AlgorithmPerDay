from sys import stdin

input == stdin.readline
a, b = map(int, input().split())

def prime(n):
  if n == 1:
    return False

  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False

  return True

for j in range(a, b + 1):
  if prime(j):
    print(j)
    
