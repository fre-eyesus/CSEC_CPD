game = int(input())
winner = input()

a = 0
d = 0
for i in range(game):
    if winner[i] == "A":
        a += 1
    elif winner[i] == "D":
        d += 1

if a > d:
    print('Anton')
elif a < d:
    print('Danik')
else:
    print('Friendship')
