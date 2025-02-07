a, b, c, d = map(int, input().split())
s = input()
calorie = {'1': a, '2': b, '3': c, '4': d}

calorie_sum = 0
for cal in s:
    calorie_sum += calorie[cal]  

print(calorie_sum)
