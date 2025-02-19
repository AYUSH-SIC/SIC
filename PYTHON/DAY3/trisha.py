n = int(input())
orange_list = input().split()
i,k = 0,0
for i in range(n):
    if(int(orange_list[i]) < int(orange_list[n-1])):
        orange_list[i],orange_list[k] = orange_list[k],orange_list[i]
        k += 1
orange_list[k],orange_list[-1] = orange_list[-1],orange_list[k]
print(' '.join(orange_list))