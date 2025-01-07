class User:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
users = [User(name, int(height), int(weight)) for name,height,weight in arr]

users.sort(key=lambda x: (x.height, -x.weight)) # 키는 오름차순, 무게는 내림차순

for user in users:
    print(f'{user.name} {user.height} {user.weight}')
