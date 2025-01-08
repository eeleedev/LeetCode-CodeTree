class Student:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())
arr = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

students = [Student(height,weight,number) for height,weight,number in arr]
students.sort(key=lambda x: (x.height, -x.weight))

for student in students:
    print(f'{student.height} {student.weight} {student.number}')