n = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(nums)
reversed_nums = sorted_nums[::-1]

print(" ".join(map(str,sorted_nums)))
print(" ".join(map(str,reversed_nums)))