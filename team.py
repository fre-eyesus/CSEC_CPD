num = int(input())
flag = 0 

for _ in range(num):
    l = input().split(" ")
    line = list(map(int, l))

    
    for j in range(len(line) - 2):  
        if (line[j] == 1 and line[j + 1] == 1):  
            flag += 1
        elif (line[j] == 1 and line[j + 2] == 1):  
            flag += 1
        elif (line[j + 1] == 1 and line[j + 2] == 1):
            flag += 1

print(flag)
