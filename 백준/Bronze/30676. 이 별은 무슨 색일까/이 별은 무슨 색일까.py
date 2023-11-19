import itertools


l = [380, 425, 450, 495, 570, 590, 620, 781]
c = ['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']

n = int(input())

for i, (nm, color) in enumerate(itertools.zip_longest(l, c), 1):
    if l[i - 1] <= n < l[i]:
        if i == len(l):
            print(c[-1])
        else:   
            print(color)