n = list(map(int,input().split()))

friend_no = n[0]
fence_height = n[1]

friends_height = list(map(int,input().split()))

width = 0
for i in range(len(friends_height)):
    if friends_height[i] > fence_height:
        width += 2
    else:
        width +=1

print(width)
