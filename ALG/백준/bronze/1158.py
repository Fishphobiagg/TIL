N, K = map(int, input().split())

original_num_list = [i for i in range(1, N+1)]
num_list = [i for i in range(1, N+1)]
josephus = []
idx = K-1
remove_idx = 0
while len(josephus) < N:
    if len(num_list) - idx+1 > idx+1:
        josephus.append(num_list[idx])
        idx += K
        print(original_num_list)
        original_num_list.remove(josephus[remove_idx])
        remove_idx += 1
    else:
        num_list += original_num_list

print("<", end="")
for i in range(len(josephus)-1):
  print(josephus[i], end=", ")
print(str(josephus[len(josephus)-1])+">")

