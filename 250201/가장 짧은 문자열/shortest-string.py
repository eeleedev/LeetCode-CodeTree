str1 = input()
str2 = input()
str3 = input()

max_len = max(len(str1), len(str2), len(str3))
min_len = min(len(str1), len(str2), len(str3))

print(max_len-min_len)