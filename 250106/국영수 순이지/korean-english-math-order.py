class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
students = [Student(name,kor,eng,math) for name,kor,eng,math in arr]

students.sort(key=lambda x: (x.kor, x.eng, x.math), reverse=True) # 기본은 내림차순

for student in students:
    print(student.name, student.kor, student.eng, student.math)

# Write your code here!