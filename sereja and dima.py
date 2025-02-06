n = int(input())
cards = list(map(int, input().split()))

left = 0  
right = n - 1 
s_sum = 0
d_sum = 0
turn = 0

while left <= right:
    if cards[left] >= cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1

    if turn == 0:
        s_sum += chosen  
    else:
        d_sum += chosen

    turn = 1 - turn  

print(s_sum, d_sum)