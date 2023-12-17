from sys import stdin
import math

input = stdin.readline
a, b = map(int, input().split())
print(math.gcd(a, b))
print(math.lcm(a, b))
