column = int(input())
block = list(map(int,input().split()))
srt = sorted(block)

print(*srt, sep = " ")
