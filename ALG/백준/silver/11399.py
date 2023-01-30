N = int(input())
time = list(map(int, input().split()))
time = sorted(time)
ind_time = 0
total = 0
for i in time:
    ind_time +=i
    total += ind_time
    
print(total)