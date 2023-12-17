from sys import stdin

while True:
    nums = input().strip()

    if nums == "0":
        break
    if nums == nums[::-1]:
        print("yes")
    else:
        print("no")
