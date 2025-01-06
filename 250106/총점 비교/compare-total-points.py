class Student:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
students = [Student(name, *map(int,[score1,score2,score3])) for name,score1,score2,score3 in arr]

students.sort(key=lambda x: x.score1+x.score2+x.score3)

for student in students:
    print(student.name, student.score1, student.score2, student.score3)
