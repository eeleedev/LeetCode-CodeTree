n = int(input())-1
n_list = list(map(int, input().split()))
temp_max = n_list[n]

def find_max(n, n_list,temp_max):
    if n == -1:
        return temp_max

    temp = n_list[n]
    if temp > temp_max:
        temp_max = temp
    return find_max(n-1, n_list,temp_max)

print(find_max(n,n_list,temp_max))
    