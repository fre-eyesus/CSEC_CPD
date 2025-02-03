weigh =list(map(int,input().split()))         
limak = weigh[0]
bob = weigh[1]
years = 0
while bob >= limak:
  limak *= 3
  bob *= 2
  years += 1
print(years)

