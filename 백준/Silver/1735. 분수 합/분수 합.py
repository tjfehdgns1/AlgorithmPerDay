import math

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    gcd = find_gcd(numerator, denominator)
    simplified_numerator = numerator // gcd
    simplified_denominator = denominator // gcd
    return simplified_numerator, simplified_denominator

a, b = map(int, input().split())
c, d = map(int, input().split())

A, B = a * d + c * b, d * b
simple_A, simple_B = simplify_fraction(A, B)
print(simple_A, simple_B, sep=" ")