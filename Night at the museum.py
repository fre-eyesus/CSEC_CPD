string = input().strip().lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

rotations = 0
pos = 0 

for char in string:
    next_pos = alphabet.index(char)

    clockwise = (next_pos - pos) % 26
    counter = (pos - next_pos) % 26
    rotations += min(clockwise, counter)
    pos = next_pos

print(rotations)