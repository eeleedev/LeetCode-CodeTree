def solution(numbers):
    n = len(numbers)
    temp = []
    for i in range(n-1):
        for j in range(i+1, n):
            temp.append(numbers[i]+numbers[j])
            
    answer = list(set(temp))
    answer.sort()
    return answer
