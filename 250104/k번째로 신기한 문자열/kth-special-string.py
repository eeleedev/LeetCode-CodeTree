n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]
word_collector = []

# Write your code here!
for word in str:
    if t in word:
        word_collector.append(word)

sorted_collector = sorted(word_collector)
print(sorted_collector[k-1])