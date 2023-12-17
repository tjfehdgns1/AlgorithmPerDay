import sys


input = sys.stdin.readline
n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

meetings.sort(key=lambda x: (x[1], x[0]))

end_time = 0
count = 0

for start, end in meetings:
    if start >= end_time:
        end_time = end
        count += 1

print(count)
