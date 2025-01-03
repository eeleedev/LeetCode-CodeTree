n = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)
arr = []

# Write your code here!
for i in range(len(nums) // 2):
    arr.append(sorted_nums[i] + sorted_nums[len(nums) - 1 - i])
print(max(arr))
