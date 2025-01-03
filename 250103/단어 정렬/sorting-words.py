n = int(input())
word = [input() for _ in range(n)]

sorted_words = sorted(word)

for word in sorted_words:
    print(word)