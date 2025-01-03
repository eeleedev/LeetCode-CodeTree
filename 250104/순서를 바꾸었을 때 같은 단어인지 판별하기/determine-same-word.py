word1 = list(input())
word2 = list(input())

# Write your code here!
sorted_word1 = sorted(word1)
sorted_word2 = sorted(word2)

if sorted_word1 == sorted_word2:
    print('Yes')
else:
    print('No')