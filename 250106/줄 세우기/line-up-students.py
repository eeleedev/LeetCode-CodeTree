class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())
arr = [(*map(int, input().split()), i+1) for i in range(n)]
students = [Student(height, weight, number) for height, weight, number in arr]

students.sort(key=lambda x: (-x.height, -x.weight, x.number)) # 여러 개 정렬할 때는 괄호로 묶어주기

for student in students:
    print(student.height, student.weight, student.number)