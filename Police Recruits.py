event = int(input())
co = list(map(int, input().split()))

officer = 0
crime = 0

for i in range(event):
    if co[i] > 0:
        officer += co[i]  
    elif co[i] == -1:
        if officer > 0:
            officer -= 1  
        else:
            crime += 1

print(crime)
