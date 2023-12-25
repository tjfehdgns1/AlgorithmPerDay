import re

while True:
    sentence = input()

    if sentence == '#':
        break

    vowels = re.findall('[aeiouAEIOU]', sentence)

    print(len(vowels))