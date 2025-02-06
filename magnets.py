no_magnets = int(input())
magnets = []
for i in range(no_magnets):
    magnet = input()
    magnets.append(magnet)

counter = 1 
for i in range(len(magnets) - 1):
    if magnets[i] != magnets[i + 1]:
        counter += 1

print(counter)