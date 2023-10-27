from sys import stdin
input = stdin.readline

n = int(input())
words = set(input().strip() for _ in range(n))

sorted_words = sorted(words, key=lambda x: (len(x), x))

print(*sorted_words)
