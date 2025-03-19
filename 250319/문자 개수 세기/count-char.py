string = input()
word = input()
result = 0

for elem in string:
    if elem == word:
        result += 1

print(result)